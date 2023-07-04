const mongoose = require('mongoose')

const schema = mongoose.Schema

const diabete = new schema({
    pregnancy:Number,
    glucozo:Number,
    age:Number,
    BMI:Number,
    diabeteFunction:{typeof: Number, default:3},
    insulin:Number,
    bloodPresure:Number,
    height:{typeof : Number, default :170}
})
module.exports = mongoose.Model('diabete',diabete)

