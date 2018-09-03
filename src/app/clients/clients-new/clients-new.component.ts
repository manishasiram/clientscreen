import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-clients-new',
  templateUrl: './clients-new.component.html',
  styleUrls: ['./clients-new.component.css']
})
export class ClientsNewComponent implements OnInit {

  clientFeeId: String;
  constructor() { }

  ngOnInit() {
    this.clientFeeId = 'Lighthouse';
  }

  displayClientFee(clientFee) {
    this.clientFeeId = clientFee;
    console.log(clientFee, 'test');
  }
}
