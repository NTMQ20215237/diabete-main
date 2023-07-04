const mongoose = require('mongoose');
 
 async function connect(){
        try {
          await mongoose.connect('mongodb://localhost:27017/diabete')
          console.log('connect successfully  !!!')  
        }catch (error) {
          console.log('connect failed !!!')  
        }
  }
module.export = {connect}
