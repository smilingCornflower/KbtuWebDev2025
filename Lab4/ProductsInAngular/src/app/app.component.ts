import {Component} from '@angular/core';
import {RouterOutlet} from '@angular/router';
import {ProductsComponent} from './components/products/products.component';
import {AddProductComponent} from './components/add-product/add-product.component';

@Component({
    selector: 'app-root',
    imports: [RouterOutlet, ProductsComponent, AddProductComponent],
    templateUrl: './app.component.html',
    styleUrl: './app.component.css',
})
export class AppComponent {
    title = 'ProductsInAngular';
}
