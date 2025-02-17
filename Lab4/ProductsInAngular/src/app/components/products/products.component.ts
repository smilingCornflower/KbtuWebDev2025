import {Component} from '@angular/core';
import {Product} from '../../models/product.model';
import {ProductService} from '../../services/product.service';

import {NgForOf} from '@angular/common';

@Component({
    selector: 'app-products',
    imports: [
        NgForOf,
    ],
    templateUrl: './products.component.html',
    styleUrl: './products.component.css',
})
export class ProductsComponent {
    products: Product[] = [];

    constructor(private productService: ProductService) {
    }

    ngOnInit() {
        this.productService.getProducts().subscribe({
                next: (data) => this.products = data,
                error: (error) => console.log(error),
            },
        );
    }
    shareToTelegram(product: Product) {
        window.open(`https://t.me/share/url?url=${encodeURIComponent(product.link)}`, '_blank');
    }

    shareToWhatsApp(product: Product) {
        window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(product.name)} ${encodeURIComponent(product.link)}`, '_blank');
    }
}
