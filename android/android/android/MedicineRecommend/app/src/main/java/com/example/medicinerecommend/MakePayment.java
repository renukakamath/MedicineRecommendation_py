package com.example.medicinerecommend;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONObject;

public class MakePayment extends AppCompatActivity implements JsonResponse {
    EditText e1,e2,e3,e4;
    Button b1;
    String logid ,quantity,card,cvv;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_make_payment);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1=(EditText) findViewById(R.id.amount);
        e3=(EditText)findViewById(R.id.card) ;
        e4=(EditText)findViewById(R.id.cvv);
        b1=(Button) findViewById(R.id.payment);
        e1.setText(Viewbookings.amt);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                card=e3.getText().toString();
                cvv=e4.getText().toString();

                if(card.equalsIgnoreCase("")|| card.length()!=16)
                {
                    e3.setError("Enter your 16 digits card number");
                    e3.setFocusable(true);
                }

                else if(cvv.equalsIgnoreCase("")|| cvv.length()!=3)
                {
                    e4.setError("Enter your 3 digits C V V ");
                    e4.setFocusable(true);
                }

                else {


                    JsonReq JR = new JsonReq();
                    JR.json_response = (JsonResponse) MakePayment.this;
                    String q = "/Makepayment?bid=" + Viewbookings.bid + "&amt=" + Viewbookings.amt + "&login_id=" + sh.getString("log_id", "")+"&mid=" + Viewbookings.mid;
                    q = q.replace(" ", "%20");
                    JR.execute(q);
                }
            }
        });
    }

    @Override
    public void response(JSONObject jo) {
        try {
            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                Toast.makeText(getApplicationContext(), " SUCCESS", Toast.LENGTH_LONG).show();
                startActivity(new Intent(getApplicationContext(), Userhome.class));

            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),Userhome.class);
        startActivity(b);
    }
    }
