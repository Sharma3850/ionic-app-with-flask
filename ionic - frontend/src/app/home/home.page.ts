import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';


@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
})
export class HomePage implements OnInit {
  updatesData: any;
  // updates: any;
  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getUpdates().subscribe(
      data => {
        this.updatesData = data;
        console.log('Fetched updates:', this.updatesData);
      },
      error => {
        console.error('Error fetching updates', error);
      }
    );
  }

  // getUpdates(){
  //   this.dataService.getUpdates().subscribe({
  //     next:(data:any)=>{
  //       console.log('API response:', data);
  //     },
  //     error:(error:any)=>{
  //       console.error('Error fetching data', error);
  //     }
  //   })
  // }

  // onSubmit(){
  //   let obj:any=    {
  //     "name":"Yogesh",
  //     "id":1
  //   }
    // {
    //   "name":"tezin",
    //   "id":2
    // }
  // ]

  // this.dataService.postData(obj).subscribe({
  //   next:(response:any)=>{
  //     console.log("reponse value is",response);
  //   },
  //   error:(error:any)=>{
  //     console.log("errir value is",error);
  //   }
  // })
    

  }


