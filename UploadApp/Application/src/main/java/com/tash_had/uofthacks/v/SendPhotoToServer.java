package com.tash_had.uofthacks.v;

import android.graphics.Color;
import android.os.AsyncTask;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.HashMap;

import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;


public class SendPhotoToServer {
    static OkHttpClient client = new OkHttpClient();
    static String SERVER = "http://100.64.223.5:5000";


    void sendPhoto(HashMap<String, String> jsonData) throws IOException{
        JSONObject picDataJson = new JSONObject();
        try {
            Toast.makeText(GlobalVariables.cameraActivity, GlobalVariables.fullUserName, Toast.LENGTH_SHORT).show();
            picDataJson.put("uuid", GlobalVariables.uuid);
            picDataJson.put("name", GlobalVariables.fullUserName);
            picDataJson.put("gender", GlobalVariables.userGender);
            for (String key : jsonData.keySet()){
                picDataJson.put(key, jsonData.get(key));
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
        new SendData().execute(picDataJson.toString());

    }

    private static String postDataToServer(String photoDataJson) throws IOException {
        okhttp3.RequestBody requestBody = new MultipartBody.Builder()
                .setType(MultipartBody.FORM)
                .addFormDataPart("data", photoDataJson)
                .build();
        okhttp3.Request request = new Request.Builder()
                .url(SERVER)
                .post(requestBody)
                .build();
        okhttp3.Response response = client.newCall(request).execute();
        return response.body().string();
    }


    class SendData extends AsyncTask<String, String, String>{
        String picData = "";
        @Override
        protected String doInBackground(String... strings) {
            String response = "";
            try {
                picData = strings[0];
                response = postDataToServer(picData);
            } catch (IOException e) {
                e.printStackTrace();
            }
            return response;
        }

        @Override
        protected void onPostExecute(String s){
            super.onPostExecute(s);
            if (s != null){
                if (s.contains("success")){
                    Toast.makeText(GlobalVariables.cameraActivity, "Clothing Added!", Toast.LENGTH_SHORT).show();
                }else if (s.contains("failure")){
                    Toast.makeText(GlobalVariables.cameraActivity, "Failure.", Toast.LENGTH_SHORT).show();
                }else{
                    Toast.makeText(GlobalVariables.cameraActivity, "1Network Error." + s, Toast.LENGTH_SHORT).show();
                }
            }else{
                Toast.makeText(GlobalVariables.cameraActivity, "Network Error", Toast.LENGTH_SHORT).show();
            }
        }
    }
}
