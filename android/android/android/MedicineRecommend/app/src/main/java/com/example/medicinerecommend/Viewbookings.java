package com.example.medicinerecommend;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Viewbookings extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {
    ListView l1;
    SharedPreferences sh;
    EditText e1;
    String[] name,ty,a,cn,n,ul,se,s,ed,value,mid_id,statu,booking_id;
    String search;
    public static  String bid,amt,mid;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewbookings);
        l1=(ListView) findViewById(R.id.list);


        l1.setOnItemClickListener(this);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) Viewbookings.this;
        String q = "/Viewbookings?log_id=" +sh.getString("log_id", "");
        q = q.replace(" ", "%20");
        JR.execute(q);
    }

    @Override
    public void response(JSONObject jo) {
        try {

            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                JSONArray ja1 = (JSONArray) jo.getJSONArray("data");
                name = new String[ja1.length()];
                ty= new String[ja1.length()];
                a= new String[ja1.length()];
                cn= new String[ja1.length()];
                n= new String[ja1.length()];
                ul= new String[ja1.length()];
                se= new String[ja1.length()];
                s= new String[ja1.length()];
                ed= new String[ja1.length()];
                value = new String[ja1.length()];
                mid_id = new String[ja1.length()];
                statu = new String[ja1.length()];
                booking_id = new String[ja1.length()];

                String[] value = new String[ja1.length()];

                for (int i = 0; i < ja1.length(); i++) {
                    name[i] = ja1.getJSONObject(i).getString("name");
                    ty[i] = ja1.getJSONObject(i).getString("ty");
                    a[i] = ja1.getJSONObject(i).getString("a");

                    cn[i] = ja1.getJSONObject(i).getString("cn");
                    n[i] = ja1.getJSONObject(i).getString("n");
                    ul[i] = ja1.getJSONObject(i).getString("ul");
                    se[i] = ja1.getJSONObject(i).getString("se");
                    s[i] = ja1.getJSONObject(i).getString("s");
                    mid_id[i] = ja1.getJSONObject(i).getString("medicine_id");
                    ed[i] = ja1.getJSONObject(i).getString("ed");
                    statu[i] = ja1.getJSONObject(i).getString("status");
                    booking_id[i]= ja1.getJSONObject(i).getString("booking_id");
                    value[i] =  "Medicine:" + name[i]+ "\nType:" + ty[i] + "\nAmount:" + a[i]  + "\nChemical Name:" + cn[i] + "\nNature:" + n[i] +"\nUnique Label:" + ul[i]  +"\nSide Effect:" + se[i] +"\nStorage:" + s[i]  +"\nstatus:" + statu[i] ;

                }

                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), R.layout.custtext, value);

                l1.setAdapter(ar);


            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();

        }
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
bid=booking_id[i];
amt=a[i];

mid=mid_id[i];
        final CharSequence[] items = {"Payment", "Cancel"};

        AlertDialog.Builder builder = new AlertDialog.Builder( Viewbookings.this);
        builder.setItems(items, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int item) {

                if (items[item].equals("Payment")) {
                  startActivity(new Intent(getApplicationContext(),MakePayment.class));

                } else if (items[item].equals("Cancel")) {
                    dialog.dismiss();
                }
            }

        });
        builder.show();

    }
    }
