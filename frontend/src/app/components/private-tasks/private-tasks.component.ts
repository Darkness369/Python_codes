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
   
  user = {
    id: '',
    username: ''
    
  } 

  ngOnInit() {
    this.getUsers()
  }

  
  deleteUsers(usuario){
    this.taskService.DeleteUser(usuario).subscribe(res => console.log(JSON.stringify(res)));
    this.getUsers();
  }
  
  update(usuario){
    let input = prompt(`Introduce el nuevo nombre de usuario`);
    this.user.id = usuario
    this.user.username = input;
    this.taskService.Update(this.user).subscribe(res => console.log(JSON.stringify(res)));
    this.getUsers();
  }

  getUsers() {
    let resp = this.auth.getUsers();
    resp.subscribe((res) => {
      this.auth.DatosUser = res;
    })
  }

}
