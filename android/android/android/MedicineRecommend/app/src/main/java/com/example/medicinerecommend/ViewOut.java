package com.example.medicinerecommend;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class ViewOut extends AppCompatActivity implements JsonResponse{

    EditText e1,e2,e3,e4,e5,e6,e7,e8,e9;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_out);
        e1=(EditText) findViewById(R.id.etmedicine);
        e2=(EditText) findViewById(R.id.etmanuf);
        e3=(EditText) findViewById(R.id.etmnuplace);
        e4=(EditText) findViewById(R.id.etdis);
        e5=(EditText) findViewById(R.id.etdisplace);
        e6=(EditText) findViewById(R.id.etpharm);
        e7=(EditText) findViewById(R.id.etphramplace);
        e8=(EditText) findViewById(R.id.etmfg);
        e9=(EditText) findViewById(R.id.etexp);


        JsonReq JR=new JsonReq();
        JR.json_response=(JsonResponse) ViewOut.this;
        String q = "/ViewOut?out="+AndroidBarcodeQrExample.vals;
        q=q.replace(" ","%20");
        JR.execute(q);



    }

    @Override
    public void response(JSONObject jo) {

        try {

            String method=jo.getString("method");
            if(method.equalsIgnoreCase("ViewOut")) {
                String status = jo.getString("status");
                Log.d("pearl", status);
                Toast.makeText(getApplicationContext(), status, Toast.LENGTH_SHORT).show();
                if (status.equalsIgnoreCase("success")) {
                    e1.setText( jo.getString("medicine"));
                    e2.setText( jo.getString("manu"));
                    e3.setText( jo.getString("manuplace"));
                    e4.setText( jo.getString("dis"));
                    e5.setText( jo.getString("displace"));
                    e6.setText( jo.getString("phar"));
                    e7.setText( jo.getString("pharplace"));
                    e8.setText( jo.getString("mfg"));
                    e9.setText( jo.getString("exp"));

//                    CustimageOwner clist=new CustimageOwner(this,image,ownername,place,phone,email);
//                    lv1.setAdapter(clist);

                } else {
                    Toast.makeText(getApplicationContext(), "no data", Toast.LENGTH_LONG).show();

                }


            }




        }catch (Exception e)
        {
            // TODO: handle exception

            Toast.makeText(getApplicationContext(),e.toString(), Toast.LENGTH_LONG).show();
        }


    }
}