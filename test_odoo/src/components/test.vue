<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})





</script>


<template>



  <div class="header">
   <div class="icon" >
   <img src="../assets/Elements/R3 Factory Logo.png"/>
   </div>
   <div class="icon2">
   <img src="../assets/Elements/Header Icons/Search bar (when not clicked).png"/>
   </div>
   <div class="icon3">
   <img src="../assets/Elements/Header Icons/Arabic lang - when not clicked.png"/>
   </div>
   <div class="icon4">
   <img src="../assets/Elements/Header Icons/Orders (when not clicked).png"/>
   </div>
    <div class="icon5">
   <img src="../assets/Elements/Header Icons/Cart (when not clicked).png"/>
   </div>
    <div class="icon6">
   <img src="../assets/Elements/Header Icons/Sign in (when not clicked).png"/>
   </div>
     
  </div>

  <div class="body">
    <div class="menu">
        <div class="m">
            <h2>Repair</h2>
        </div>
        <div class="m">
            <h2>Renew</h2>
        </div>
        <div class="m2">
            <h2>Reuse</h2>
        </div>

    </div>
  <div class="menu2">
        <div class="m3">
            <h2>Buy</h2>
        </div>
        <div class="m4">
            <h2>Sell</h2>
        </div>
       

    </div>

    <div class="rcorners2">



      <div class="item_details">

        <div class="ct_adress">
          <p><b>All Categories > Mobile</b></p>

        </div>

        <div class="product_n_b">
         <div class="n_product">

          
  <br>
<div class="data">
    <div v-for="post in posts">
      <h3>{{ product_value = post}}
      
      
      </h3>
    </div>
    <div class="model"></div>
    <div v-for="post2 in posts2" >
      <h3>  {{ product_value = post2}}
      
      
      </h3>
    </div>
  </div>
  
        </div>
        <div class="vrf_btn">
          <h4>Verified</h4>
        </div>

        </div>
      </div>

      <div class="details">

        <div class="s">

        <div class="s1">
          <img src="../assets/Elements/d.jpg" />
        </div>

      <div class="s2">
          <img src="../assets/Elements/e.jpg" />
        </div>

        </div>

        <div class="main_img">
            <img src="../assets/Elements/d.jpg"/>
        </div>

        <div class="mw3">
          <h2><b>3 months of warranty</b></h2>
        </div>


   <div class="dropdown">
  <button class="dropbtn">1</button>
  <div class="dropdown-content">
    <a href="#">1</a>
    <a href="#">2</a>
    <a href="#">3</a>
  </div>
</div>
 
      <div class="g1">
        <div class="g2">
        <div class="pre_btn">
          <h4>Pre-Owned</h4>
        </div>
        
        <div class="price">
          <h2><b>AED 2999.00</b></h2>
        </div>
        </div>
          
      <div class="sold">
        <img src="../assets/Elements/g.png"/>
        <h5>Three Business Days</h5>
      </div>
      <div class="sold2">
        <img src="../assets/Elements/f.png"/>

        <h5>Sold By R3 Factory</h5>
      </div>


      <div class="procced_button">
        <h3><b>  Proceed to Checkout  </b></h3>
      </div>







      </div>
      
      
      </div>
<hr>

      <div class="Pre-owned">
        <h4><b>Pre-owned A( Slightly Used )</b></h4>
      </div>

   <div class="text">
        <h5><b>Item has been slightly used | minimal scratches | compatible accessories | tested by experts | 12 Months Warranty
        </b></h5>

      </div>
<hr>

 <div class="text2">
        <h3><b>Description</b></h3>

      </div>
  <div class="text">

       <div class="data">
    
    <div class="model"></div>
    <div v-for="post3 in posts3" >
      <h3>  {{ product_value = post3}}
      
      
      </h3>
    </div>
  </div>

      </div>

<hr>
<div class="text2">
        <h3><b>Alternate Options</b></h3>

      </div>


<div class="foot">

<div class="ao">

  <div class="ao1">
<div class="vrf_btn2">
          <h5>Verified</h5>
        </div>

        <div class="ao_img">
          <img src="../assets/Elements/Header Icons/Cart Icon (when not clicked) copy.png">
        </div>
</div>
<div class="ao2">
<div class="vrf_btn3">
          <h5>Brand New</h5>
        </div>

        <div>
          <h5>AED 3999.00</h5>
        </div>
</div>

<div class="ao3">
   <div class= "instock">
          <p>in stock</p>
        </div>
<div class="procced_button2">
        <h5><b>  Buy Now  </b></h5>
      </div>

       
</div>



</div>


<div class="ao">

  <div class="ao1">
<div class="vrf_btn2">
          <h5>Verified</h5>
        </div>

        <div class="ao_img">
          <img src="../assets/Elements/Header Icons/Cart Icon (when not clicked) copy.png">
        </div>
</div>
<div class="ao2">
<div class="vrf_btn3">
          <h5>Brand New</h5>
        </div>

        <div>
          <h5>AED 3999.00</h5>
        </div>
</div>

<div class="ao3">
   <div class= "instock">
          <p>in stock</p>
        </div>
<div class="procced_button2">
        <h5><b>  Buy Now  </b></h5>
      </div>

       
</div>



</div>

<div class="ao">

  <div class="ao1">
<div class="vrf_btn2">
          <h5>Verified</h5>
        </div>

        <div class="ao_img">
          <img src="../assets/Elements/Header Icons/Cart Icon (when not clicked) copy.png">
        </div>
</div>
<div class="ao2">
<div class="vrf_btn3">
          <h5>Brand New</h5>
        </div>

        <div>
          <h5>AED 3999.00</h5>
        </div>
</div>

<div class="ao3">
   <div class= "instock">
          <p>in stock</p>
        </div>
<div class="procced_button2">
        <h5><b>  Buy Now  </b></h5>
      </div>

       
</div>



</div>
<div class="ao">

  <div class="ao1">
<div class="vrf_btn2">
          <h5>Verified</h5>
        </div>

        <div class="ao_img">
          <img src="../assets/Elements/Header Icons/Cart Icon (when not clicked) copy.png">
        </div>
</div>
<div class="ao2">
<div class="vrf_btn3">
          <h5>Brand New</h5>
        </div>

        <div>
          <h5>AED 3999.00</h5>
        </div>
</div>

<div class="ao3">
   <div class= "instock">
          <p>in stock</p>
        </div>
<div class="procced_button2">
        <h5><b>  Buy Now  </b></h5>
      </div>

       
</div>



</div>

<div class="ao">

  <div class="ao1">
<div class="vrf_btn2">
          <h5>Verified</h5>
        </div>

        <div class="ao_img">
          <img src="../assets/Elements/Header Icons/Cart Icon (when not clicked) copy.png">
        </div>
</div>
<div class="ao2">
<div class="vrf_btn3">
          <h5>Brand New</h5>
        </div>

        <div>
          <h5>AED 3999.00</h5>
        </div>
</div>

<div class="ao3">
   <div class= "instock">
          <p>in stock</p>
        </div>
<div class="procced_button2">
        <h5><b>  Buy Now  </b></h5>
      </div>

       
</div>



</div>



</div>





    </div>
  </div>
  
</template>

<style scoped>

.data{
    display: flex;


}

.model{
  margin-left: 10px;
}

.header {

  display: flex;
  align-items: center;
  justify-content: space-around;
 
}
.icon img{
    max-height: 50px;
    margin-right: 40px;
}
.icon2 img{
    max-height: 40px;
    margin-right: 40px;

}
.icon3 img{
    max-height: 20px;
    margin-right: 40px;

}
.icon4 img{
    max-height: 20px;
    margin-right: 40px;

}

.icon5 img{
    max-height: 20px;
    margin-right: 40px;

}
.icon6 img{
    max-height: 20px;
    margin-right: 40px;

}

.menu{
  
  display: flex;
  font-size: large;
  align-items: center;
  justify-content: space-around;
  
}

.m{
    margin-right: 3px;

    flex: 1;
    border: 1px solid #39A536;
    text-align: center;
    color: #39A536;
    text-decoration: solid;
}

.m2{

    flex: 1;
    border: 1px solid #39A536;
    background-color: #39A536;
    text-align: center;
    color: white;
}


.m3{
  margin-right: 3px;
    flex: 1;
    border: 1px solid #39A536;
    background-color: #39A536;
    text-align: center;
    color: white;
    text-decoration: solid;
}

.m4{
    flex: 1;
    border: 1px solid gray;
    background-color: gray;
    text-align: center;
    color: #3E3D37;
}


.menu2{
  display: flex;
  justify-content: space-around;
  margin-top: 3px;
  font-size: large;
  font-family: "Avenir";
  src: local("Avenir"),
   url(../assets/Elements/fonts/Avenir.ttc) format("truetype");
  align-items: center;
}

.rcorners2 {
  margin-top: 10px;
  border-radius: 10px;
  border: 0.2px solid #39A536;
  padding: 20px; 
  height:700px;  

}

.s1 img{
  border-radius: 10px;
  border: 2px solid #000000;
  padding: 20px; 
  height:100px;  
  width: 100px;
  margin-top: 5px;
}

.s2 img{
  border-radius: 10px;
  border: 2px solid #000000;
  padding: 20px; 
  height:100px;  
  width: 100px;
}
.product_n_b{
    display: flex;
    align-items: center;
    justify-content: space-between;

}

.vrf_btn {
    border: 8px solid #39A536;    
    background-color: #39A536;
    color: white;
    text-align: right;
}


.mw3{
  color: #39A536;
   height: 200px;
  display: flex;
  
}
.mw3 h2{
  align-self: flex-end;

}

.n_product {
    margin-left: 20px;

}

.details{
  margin-top: 25px;
  margin-left: 25px;
  display: flex;
  align-items: center;
}

.main_img img{
  margin-left: 20px;
  height:240px;  
  width: 300px;
  
}


.count {
    height: 400px;
}

.pre_btn{
border-radius: 5px;
  border: 1px solid #39A536;
  background-color: #39A536;
  color: white;
  padding: 5px;
  text-align: center;

}

.sold{

  margin-top: 25px;
  display: flex;
}

.sold2{
  margin-top: 15px;
  display: flex;
}

.g1{
  align-items: center;
  margin-left: 30px;
}

.g2{
  display: flex;
}

.price{
  margin-left: 30px;
}

.procced_button{
  border-radius: 30px;
  border: 1px solid #39A536;
  color: #39A536;
  padding: 13px;
  text-align: center;
  margin-top: 40px;
  margin-left: 50px;
}

.procced_button2{
  border-radius: 30px;
  border: 1px solid #39A536;
  color: #39A536;
  text-align: center;
  padding: 5px;
  margin-left: 20px;
}
.sold img{
  width: 20px;
  height: 20px;
  margin-right: 10px;
}
.sold2 img{
  width: 20px;
  height: 20px;
  margin-right: 10px;

}


.dropbtn {
  background-color: white;
  color: rgb(0, 0, 0);
  padding: 16px;
  font-size: 16px;
  border: 1px solid #39A536;
}

.dropdown {
  margin-left: 40px;
  margin-right: 40px;
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: #ddd;}

.dropdown:hover .dropdown-content {display: block;}

.dropdown:hover .dropbtn {background-color: #3e8e41;}

.Pre-owned{
  margin-left: 10px;
  margin-top: 8px;
  width: 250px;
  border-radius: 5px;
  border: 1px solid #39A536;
  background-color: #39A536;
  color: white;
  padding: 5px;
  text-align: center;
}
.text{
  margin-left: 10px;
  margin-top: 8px;
  margin-bottom: 20px;
}

.text2{
  margin-left: 10px;
  margin-top: 8px;
}


.ao{
  margin-top: 10px;
  justify-content: space-around;
  border: 0.5px solid #39A536;
  padding: 5px; 
  width: 200px;
  height:110px; 
}

.ao1{
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.ao2{
  display: flex;
  margin-top: 10px;
  justify-content: space-between;
}

.ao3{
  align-items: center;
  display: flex;
  margin-top: 10px;
}

.ao3 p{
  font-size: 10px;
  
}

.ao3 h5{
  font-size: 13px;
}


.vrf_btn2{
     text-align: center; 
    width: 60px;
    align-items: center;
    background-color: #39A536;
    color: white;
}




.vrf_btn3{
    text-align: center; 
    width: 80px;
    align-items: center;
    background-color: #39A536;
    color: white;
}

.vrf_btn3 h5{
    text-align: center; 
    width: 80px;
    align-items: center;
    background-color: #39A536;
    color: white;
}

.ao_img img{
  width: 12px;
}


.m4 h2{
  font-size: smaller;
  padding: 10px;
}

.foot{
  display: flex;
  justify-content: space-around;
}

.shadow{
  filter: drop-shadow(0px 0px 7px rgba(0, 0, 0, 0.7));
  margin-bottom: 5px;
  width: 100%;
}


</style>
<script>
import axios from 'axios'

export default {
  name: 'PostList',
  created() {
    this.getPosts()
    this.getPosts2()
    this.getPosts3()


  },
  data() {
    return {
      posts: [],
      post2:[],
      post3:[],
      errorMsg: '',
    }
  },
  methods: {
    getPosts() {
      axios
        .get('http://localhost:8069/r3/records/')
        .then((response) => {
          console.log(response)
          this.posts = response.data
        })
        .catch((error) => {
          console.log(error)
          this.errorMsg = 'Error retrieving data'
        })
    },
     getPosts2() {
      axios
        .get('http://localhost:8069/r3/model/')
        .then((response) => {
          console.log(response)
          this.posts2 = response.data
        })
        .catch((error) => {
          console.log(error)
          this.errorMsg = 'Error retrieving data'
        })
    },
     getPosts3() {
      axios
        .get('http://localhost:8069/r3/des/')
        .then((response) => {
          console.log(response)
          this.posts3 = response.data
        })
        .catch((error) => {
          console.log(error)
          this.errorMsg = 'Error retrieving data'
        })
    },
  },



}




</script>
