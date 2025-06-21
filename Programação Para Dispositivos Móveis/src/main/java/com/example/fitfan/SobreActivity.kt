package com.example.fitfan

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import androidx.activity.ComponentActivity

class SobreActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.sobre_activity)

        val imageView = findViewById<ImageView>(R.id.iv_foto)
        val btnVoltar = findViewById<Button>(R.id.btn_voltar)

        imageView.setImageResource(R.drawable.minha_foto)

        btnVoltar.setOnClickListener {
            startActivity(Intent(this, MainActivity::class.java))
        }
    }
}