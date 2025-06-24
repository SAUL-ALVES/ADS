package com.example.healthychef

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.MediaController
import android.widget.TextView
import android.widget.Toast
import android.widget.VideoView
import androidx.activity.ComponentActivity
import androidx.core.net.toUri

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        val etPeso = findViewById<EditText>(R.id.etPeso)
        val etAltura = findViewById<EditText>(R.id.etAltura)
        val btnCalcularIMC = findViewById<Button>(R.id.btnCalcularIMC)
        val tvResultadoIMC = findViewById<TextView>(R.id.tvResultadoIMC)
        val ivFaixaIMC = findViewById<ImageView>(R.id.ivFaixaIMC)

        val videoViewReceita = findViewById<VideoView>(R.id.videoViewReceita)

        val etNomeReceita = findViewById<EditText>(R.id.etNomeReceita)
        val btnConfirmarReceita = findViewById<Button>(R.id.btnConfirmarReceita)
        val ivImagemReceita = findViewById<ImageView>(R.id.ivImagemReceita)
        val tvCalorias = findViewById<TextView>(R.id.tvCalorias)

        val btnLimpar = findViewById<Button>(R.id.btnLimpar)

        val btnNavegarReceitas = findViewById<Button>(R.id.btnNavegarReceitas)
        val btnNavegarSobre = findViewById<Button>(R.id.btnNavegarSobre)


        val videoPath = "android.resource://${packageName}/${R.raw.smoothie_video}"
        val uri = videoPath.toUri()
        videoViewReceita.setVideoURI(uri)
        val mediaController = MediaController(this)
        mediaController.setAnchorView(videoViewReceita)
        videoViewReceita.setMediaController(mediaController)
        videoViewReceita.start()


        btnCalcularIMC.setOnClickListener {
            val pesoStr = etPeso.text.toString()
            val alturaStr = etAltura.text.toString()

            if (pesoStr.isNotEmpty() && alturaStr.isNotEmpty()) {
                val peso = pesoStr.toFloat()
                val altura = alturaStr.toFloat()

                if (altura > 0) {
                    val imc = peso / (altura * altura)
                    tvResultadoIMC.text = "Seu IMC: %.2f".format(imc)
                    tvResultadoIMC.visibility = View.VISIBLE
                    ivFaixaIMC.visibility = View.VISIBLE


                    when {
                        imc < 18.5 -> ivFaixaIMC.setImageResource(R.drawable.imc_baixo_peso)
                        imc < 24.9 -> ivFaixaIMC.setImageResource(R.drawable.imc_normal)
                        imc < 29.9 -> ivFaixaIMC.setImageResource(R.drawable.imc_sobrepeso)
                        else -> ivFaixaIMC.setImageResource(R.drawable.imc_obesidade)
                    }
                } else {
                    Toast.makeText(this, "A altura deve ser maior que zero!", Toast.LENGTH_SHORT).show()
                }
            } else {
                Toast.makeText(this, "Preencha o peso e a altura.", Toast.LENGTH_SHORT).show()
            }
        }


        btnConfirmarReceita.setOnClickListener {
            val nomeReceita = etNomeReceita.text.toString().trim()


            if (nomeReceita.lowercase() == "smoothie de banana") {
                ivImagemReceita.setImageResource(R.drawable.smoothie_banana)
                tvCalorias.text = "Aprox. 250 kcal"
                ivImagemReceita.visibility = View.VISIBLE
                tvCalorias.visibility = View.VISIBLE
            } else {
                Toast.makeText(this, "Digite: smoothie de banana", Toast.LENGTH_SHORT).show()
                ivImagemReceita.visibility = View.GONE
                tvCalorias.visibility = View.GONE
            }
        }


        btnLimpar.setOnClickListener {

            etPeso.text.clear()
            etAltura.text.clear()
            etNomeReceita.text.clear()


            tvResultadoIMC.visibility = View.GONE
            ivFaixaIMC.visibility = View.GONE
            ivImagemReceita.visibility = View.GONE
            tvCalorias.visibility = View.GONE


            etPeso.requestFocus()
            Toast.makeText(this, "Campos limpos.", Toast.LENGTH_SHORT).show()
        }

        btnNavegarSobre.setOnClickListener {
            val intent = Intent(this, SobreActivity::class.java)
            startActivity(intent)
        }

        btnNavegarReceitas.setOnClickListener {
            val intent = Intent(this, ReceitasRapidas::class.java)
            startActivity(intent)
        }
    }
}