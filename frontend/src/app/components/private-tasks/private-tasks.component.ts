import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Private_taks_service } from '../../services/private-taks.service';

@Component({
  selector: 'app-private-tasks',
  templateUrl: './private-tasks.component.html',
  styleUrls: ['./private-tasks.component.css']
})
export class PrivateTasksComponent implements OnInit {

  constructor(public auth:AuthService, private taskService: Private_taks_service ) {

   }
   

  ngOnInit() {
    this.getUsers()
  }

  
  deleteUsers(){
    
  }
  update(){

  }
  getUsers() {
    let resp = this.auth.getUsers();
    resp.subscribe((res) => {
      this.auth.DatosUser = res;
      console.log(res);
    })
  }

}
