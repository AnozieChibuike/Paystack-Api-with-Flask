console.log('I Pledge my allegiance to the royal emperor')

function payWithPaystack(e) {
//  e.preventDefault();

  let handler = PaystackPop.setup({
    key: 'pk_test_bb270a3a924f501bcf9020de2870fb4a0ea4eee6', // Replace with your public key
    email: 'chibuikeanozie0@gmail.com',
    amount: 100 * 100,
    ref: 'apacomu', // generates a pseudo-unique reference. Please replace with a reference you generated. Or remove the line entirely so our API will generate one for you
    // label: "Optional string that replaces customer email"
    onClose: function(){
      alert('Window closed.');
    },
    callback: function(response){
      let message = 'Payment complete! Reference: ' + response.reference;
      alert(message);
    }
  });

  handler.openIframe();
}