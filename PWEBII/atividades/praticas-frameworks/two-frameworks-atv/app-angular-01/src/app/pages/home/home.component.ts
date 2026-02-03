import { Component } from '@angular/core';
import { HeaderComponent } from '../../components/header/header.component';
import { PostComponent } from '../../components/post/post.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [HeaderComponent, PostComponent], 
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {}