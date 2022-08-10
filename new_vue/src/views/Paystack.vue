<template>
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
  
</template>

<script>
import paystack from "vue3-paystack";
import { nanoid } from "nanoid"; //if using nanoid

export default {
    name: 'Paystack',
     components: {
    paystack,
  },
  data() {
    return {
      cart: {
        items: [],
      },
        publicKey:'pk_live_e3d27b608a48267e716561ab901543ec392d958a',
        amount:100, //Expressed in lowest demonitation, so 1000kobo is equivalent to 10Naira
        email:'vic2sleek@gmail.com',
        firstname:'VIA', //optional field remember to pass as a prop of firstname if needed
        lastname:'Codes' //optional field remember to pass as a prop of lastname if needed
     };
    },
    mounted() {
    document.title = "Checkout | NelleRichPharmacy";

    this.cart = this.$store.state.cart;
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
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    
  },
}
</script>