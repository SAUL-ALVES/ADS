package com.example.fitfan

import android.net.Uri
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.MediaController
import android.widget.TextView
import android.widget.VideoView
import androidx.activity.ComponentActivity

class DicasActivity: ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.dicas_activity)

        val etDica = findViewById<EditText>(R.id.et_dica)
        val buscarDica = findViewById<Button>(R.id.btn_buscar_dica)
        val tvMensagem = findViewById<TextView>(R.id.tv_mensagem_dica)
        val vvDica = findViewById<VideoView>(R.id.vv_dica)

        val mediaController = MediaController(this)
        mediaController.setAnchorView(vvDica)
        vvDica.setMediaController(mediaController)

        buscarDica.setOnClickListener {
            val dica = etDica.text.toString().trim().lowercase()
            when (dica){
                "supino" -> {
                    tvMensagem.text = ""
                    val videoPath = "android.resource://${packageName}/${R.raw.video_supino}"
                    vvDica.setVideoURI(Uri.parse(videoPath))
                    vvDica.start()
                }
                "rosca scott" -> {
                    tvMensagem.text = ""
                    val videoPath = "android.resource://${packageName}/${R.raw.video_scott}"
                    vvDica.setVideoURI(Uri.parse(videoPath))
                    vvDica.start()
                } else -> {
                    tvMensagem.text = "Digite uma dica válida"
                    vvDica.stopPlayback()
                }
            }
        }

    }
}