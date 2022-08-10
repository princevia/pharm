<template>
  <div class="page-checkout">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Checkout</h1>
      </div>

      <div class="column is-12 box">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="item in cart.items" v-bind:key="item.product.id">
              <td>{{ item.product.name }}</td>
              <td> ₦{{ item.product.price }}</td>
              <td>{{ item.quantity }}</td>
              <td> ₦{{ getItemTotal(item).toFixed(2) }}</td>
            </tr>
          </tbody>

          <tfoot>
            <tr>
              <td colspan="2">Total</td>
              <td>{{ cartTotalLength }}</td>
              <td> ₦{{ cartTotalPrice.toFixed(2) }}</td>
            </tr>
          </tfoot>
        </table>
      </div>

  <div>
    <p class="subtitle text-is-dark"> Your order is </p>
    <h1>{{ cartTotalLength }}units</h1>
    <h1>₦{{ cartTotalPrice }}</h1>
    </div>
        <div class="column is-12 box">
        <h2 class="subtitle">Shipping details</h2>

        <p class="has-text-grey mb-4">* All fields are required</p>
          <div class="columns is-multiline">
          <div class="column is-6">
            <div class="field">
              <label>First name*</label>
              <div class="control">
                <input type="text" class="input" v-model="first_name" />
              </div>
            </div>

            <div class="field">
              <label>Last name*</label>
              <div class="control">
                <input type="text" class="input" v-model="last_name" />
              </div>
            </div>

            <div class="field">
              <label>E-mail*</label>
              <div class="control">
                <input type="email" class="input" v-model="e_mail" />
              </div>
            </div>

            <div class="field">
              <label>Phone*</label>
              <div class="control">
                <input type="text" class="input" v-model="phone" />
              </div>
            </div>
          </div>

          <div class="column is-6">
            <div class="field">
              <label>Address*</label>
              <div class="control">
                <input type="text" class="input" v-model="address" />
              </div>
            </div>
        </div>
      </div>
      <hr/>
      
          <paystack
                buttonClass="'button-class btn btn-primary'"
                buttonText="Pay Online"
                :publicKey="publicKey"
                :email="email"
                :amount="parseInt(cartTotalPrice * 100)"
                :reference="reference"
                :onSuccess="onSuccessfulPayment"
                :onCanel="onCancelledPayment"
              >
                Pay ₦{{ cartTotalPrice }}
              </paystack>
      </div>
    </div>
  </div>
</template>



<script type="application/javascript">

import paystack from "vue3-paystack";
import { nanoid } from "nanoid"; //if using nanoid

export default {
  name: "Checkout",
  components: {
    paystack,
  },
  data() {
    return {
      cart: {
        items: [],
      },
      paystack: {},
      first_name: "",
      last_name: "",
      e_mail: "",
      phone: "",
      address: "",
      errors: [],
       publicKey:'pk_live_e3d27b608a48267e716561ab901543ec392d958a',
        amount:100, //Expressed in lowest demonitation, so 1000kobo is equivalent to 10Naira
        email:'vic2sleek@gmail.com',
        firstname:'VIA', //optional field remember to pass as a prop of firstname if needed
        lastname:'Codes' //optional field remember to pass as a prop of lastname if needed
    };
  },

  mounted() {
    document.title = "Checkout | NELLRICHPharmacy";

    this.cart = this.$store.state.cart;
    
    
      
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    payWithPaystack() {
      const items = [];
      for (let i = 0; i < this.cart.items.length; i++) {
        const item = this.cart.items[i];
        const obj = {
          product: item.product.id,
          quantity: item.quantity,
          price: item.product.price * item.quantity,
        };
        items.push(obj);
      }
      const paymentOptions = {
        // general options
        
        items: items, //required
        email: this.email, //required
        amount: this.amount, //required
        reference: this.reference, //required
        currency: this.currency,
        channels: this.channels,
        metadata: this.metadata,
        label: this.label,        
        firstname: this.firstname,
        lastname: this.lastname,
      };
     
    },
  },

  computed: {
    reference: function() {
        // if using nanoid to generate randomRef
        // comment this out if not using nano id
      return nanoid(15);

    //   you can use plain JS to generate random ref ID, just uncomment this section if you
    /*
        let randomRef = "";
        let characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

        for( let i=0; i < 15; i++ )
          text += characters.charAt(Math.floor(Math.random() * characters.length));

        return randomRef;

        */
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.product.price * curVal.quantity)
      }, 0);
    },
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);

    },
  },
};
</script>