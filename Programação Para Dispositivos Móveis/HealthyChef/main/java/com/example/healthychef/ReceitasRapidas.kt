package com.example.healthychef

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.activity.ComponentActivity

class ReceitasRapidas : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_quick_recipes)

        val etBuscaReceita = findViewById<EditText>(R.id.etBuscaReceita)
        val btnBuscar = findViewById<Button>(R.id.btnBuscar)
        val ivReceitaEncontrada = findViewById<ImageView>(R.id.ivReceitaEncontrada)
        val tvIngredientes = findViewById<TextView>(R.id.tvIngredientes)

        btnBuscar.setOnClickListener {
            val nomeReceita = etBuscaReceita.text.toString().trim()

            if (nomeReceita.equals("Salada Verde", ignoreCase = true)) {
                ivReceitaEncontrada.setImageResource(R.drawable.salada_verde)
                tvIngredientes.text = "Ingredientes:\n- Folhas de alface variadas\n- Tomate\n- Pepino em rodelas\n- Cebola roxa fatiada\n- Azeite, sal e limão a gosto"
                ivReceitaEncontrada.visibility = View.VISIBLE
                tvIngredientes.visibility = View.VISIBLE
            } else {

                ivReceitaEncontrada.visibility = View.GONE
                tvIngredientes.visibility = View.GONE
                Toast.makeText(this, "Receita não cadastrada!", Toast.LENGTH_LONG).show()
            }

    }

    }
}