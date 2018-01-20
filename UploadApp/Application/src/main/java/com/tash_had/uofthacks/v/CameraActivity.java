/*
 * Copyright 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.tash_had.uofthacks.v;

import android.Manifest;
import android.content.Context;
import android.content.DialogInterface;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;

public class CameraActivity extends AppCompatActivity {
    int REQUEST_LOCATION_PERMISSION = 123;
    SharedPreferences sp;
    String GENDER_KEY = "gender";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            requestLocationPermission();
        }
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_camera);

        sp = this.getSharedPreferences("uofthacksv.clothes-upload", Context.MODE_PRIVATE);
        String gender = sp.getString(GENDER_KEY, null);
        if (gender == null){
            getGender();
        }else{
            GlobalVariables.userGender = gender;
        }
        GlobalVariables.bottomBarView = findViewById(R.id.bottom_bar);
        GlobalVariables.cameraActivity = this;

        if (null == savedInstanceState) {
            getSupportFragmentManager().beginTransaction()
                    .replace(R.id.container, BasicCameraFragment.newInstance())
                    .commit();
        }
    }

    private void requestLocationPermission() {
        requestPermissions(new String[]{Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.ACCESS_FINE_LOCATION}, REQUEST_LOCATION_PERMISSION);
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    }

    private void getGender(){
        AlertDialog.Builder genderReq = new AlertDialog.Builder(this);
        genderReq.setCancelable(false);
        genderReq.setTitle("Enter your gender");
        genderReq.setPositiveButton("Male", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                String g = "male";
                sp.edit().putString(GENDER_KEY, g).apply();
                GlobalVariables.userGender = g;

            }
        });

        genderReq.setNegativeButton("Female", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                String g = "female";
                sp.edit().putString(GENDER_KEY, g).apply();
                GlobalVariables.userGender = g;

            }
        });

        genderReq.setNeutralButton("Other", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                String g = "";
                sp.edit().putString(GENDER_KEY, g).apply();
                GlobalVariables.userGender = g;
            }
        });
        genderReq.show();
    }
//    private void printLatLon() {
//        LocationManager lm = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
//        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
//            // TODO: Consider calling
//            //    ActivityCompat#requestPermissions
//            // here to request the missing permissions, and then overriding
//            //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
//            //                                          int[] grantResults)
//            // to handle the case where the user grants the permission. See the documentation
//            // for ActivityCompat#requestPermissions for more details.
//            return;
//        }
//        Location location = lm.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);
//
//        if (location != null){
//            System.out.println( Double.toString(location.getLatitude()));
//            System.out.println( Double.toString(location.getLongitude()));
//        }
//    }

}
