package com.example.medicinerecommend;

import java.util.Locale;
import java.util.Random;

import org.json.JSONObject;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.PendingIntent;
import android.content.ActivityNotFoundException;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.speech.tts.TextToSpeech;
import android.telephony.SmsManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class AndroidBarcodeQrExample extends Activity
{
	public static String vals;
	Button b1;
	/** Called when the activity is first created. */
	String method="getslotidandlocid";
	String soapaction="http://tempuri.org/getslotidandlocid";
	SharedPreferences sh;
	static final String ACTION_SCAN = "com.google.zxing.client.android.SCAN";
	  public static TextToSpeech t1;
	@Override
	public void onCreate(Bundle savedInstanceState) 
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
//		b1=(Button)findViewById(R.id.upload);
//		b1.setOnClickListener(new View.OnClickListener() {
//			@Override
//			public void onClick(View v) {
//				startActivity(new Intent(getApplicationContext(),Uploadimage.class));
//			}
//		});
	}

	public void scanBar(View v) {
		try {
			Intent intent = new Intent(ACTION_SCAN);
			intent.putExtra("SCAN_MODE", "PRODUCT_MODE");
			startActivityForResult(intent, 0);
		} catch (ActivityNotFoundException anfe) {
			showDialog(AndroidBarcodeQrExample.this, "No Scanner Found", "Download a scanner code activity?", "Yes", "No").show();
		}
	}

	public void scanQR(View v) {
		try {
			Intent intent = new Intent(ACTION_SCAN);
			intent.putExtra("SCAN_MODE", "QR_CODE_MODE");
			startActivityForResult(intent, 0);
		} catch (ActivityNotFoundException anfe) {
			showDialog(AndroidBarcodeQrExample.this, "No Scanner Found", "Download a scanner code activity?", "Yes", "No").show();
		}
	}
//	public void Uploadfiles(View v) {
//		startActivity(new Intent(getApplicationContext(),Uploadimage.class));
//	}

	private static AlertDialog showDialog(final Activity act, CharSequence title, CharSequence message, CharSequence buttonYes, CharSequence buttonNo) {
		AlertDialog.Builder downloadDialog = new AlertDialog.Builder(act);
		downloadDialog.setTitle(title);
		downloadDialog.setMessage(message);
		downloadDialog.setPositiveButton(buttonYes, new DialogInterface.OnClickListener() {
			public void onClick(DialogInterface dialogInterface, int i) {
				Uri uri = Uri.parse("market://search?q=pname:" + "com.google.zxing.client.android");
				Intent intent = new Intent(Intent.ACTION_VIEW, uri);
				try {
					act.startActivity(intent);
				} catch (ActivityNotFoundException anfe) {

				}
			}
		});
		downloadDialog.setNegativeButton(buttonNo, new DialogInterface.OnClickListener() {
			public void onClick(DialogInterface dialogInterface, int i) 
			{
			}
		});
		return downloadDialog.show();
	}

	public void onActivityResult(int requestCode, int resultCode, Intent intent) {
		if (requestCode == 0) {
			if (resultCode == RESULT_OK) {
				String contents = intent.getStringExtra("SCAN_RESULT");
				String format = intent.getStringExtra("SCAN_RESULT_FORMAT");

//				Toast toast = Toast.makeText(this, "Content:" + contents + " Format:" + format, Toast.LENGTH_LONG);
//				toast.show();

				vals=contents;
				SharedPreferences.Editor e=sh.edit();
				e.putString("valsss",vals);
				e.commit();
				startActivity(new Intent(getApplicationContext(), ViewOut.class));
//				JsonReq JR=new JsonReq();
//				JR.json_response=(JsonResponse) AndroidBarcodeQrExample.this;
//				String q = "/verifynewfiles?fid="+sh.getString("fid","")+"&content="+vals;
//				q=q.replace(" ","%20");
//				JR.execute(q);


//				if(sh.getString("ft","").equalsIgnoreCase("Type3")) {
//					startActivity(new Intent(getApplicationContext(), ViewImage.class));
//				}
//				if(sh.getString("ft","").equalsIgnoreCase("Type4")) {
//					startActivity(new Intent(getApplicationContext(), .class));
//				}


			}
		}
	}

//	@Override
//	public void response(JSONObject jo) {
//		try {
//
//			String method=jo.getString("method");
//			if(method.equalsIgnoreCase("verifynewfiles")) {
//
//				String status = jo.getString("status");
//				Log.d("pearl", status);
//
//
//				if (status.equalsIgnoreCase("success")) {
//					Toast.makeText(getApplicationContext(), "Verified Successfully", Toast.LENGTH_LONG).show();
//
//					if(sh.getString("ft","").equalsIgnoreCase("Type3")) {
//						startActivity(new Intent(getApplicationContext(), ViewImage.class));
//					}
//					if(sh.getString("ft","").equalsIgnoreCase("Type4")) {
//						Random random = new Random();
//						String generatedPassword = String.format("%04d", random.nextInt(10000));
//
//						Log.d("MyApp", "Generated Password : " + generatedPassword);
//
//						//Getting intent and PendingIntent instance
//						Intent intent=new Intent(getApplicationContext(),MainActivity.class);
//						PendingIntent pi=PendingIntent.getActivity(getApplicationContext(), 0, intent,0);
//
////Get the SmsManager instance and call the sendTextMessage method to send message
//						SmsManager sms=SmsManager.getDefault();
//						sms.sendTextMessage("8281940635", null, "Your OTP is "+generatedPassword+"", pi,null);
//						SharedPreferences.Editor e=sh.edit();
//						e.putString("otp",generatedPassword+"");
//						e.commit();
//						startActivity(new Intent(getApplicationContext(), VerifyOTP.class));
//					}
//				} else {
//
//					Toast.makeText(getApplicationContext(), " Enterd key is not correct!!", Toast.LENGTH_LONG).show();
//					startActivity(new Intent(getApplicationContext(), Employee_view_uploaded_files.class));
//				}
//			}
//
//
//		}
//
//		catch (Exception e) {
//			// TODO: handle exception
//			e.printStackTrace();
//			Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
//		}
//	}
	public void onBackPressed()
	{
		// TODO Auto-generated method stub
		super.onBackPressed();
		startActivity(new Intent(getApplicationContext(),ip_setting.class));
	}
}