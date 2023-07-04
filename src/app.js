const express = require('express')
const app = express()
const exhbs = require('express-handlebars')
const path = require('path')
const hbs = require('handlebars')
const morgan = require('morgan')
const port = process.env.PORT || 3000
//hbd register 
hbs.registerHelper("subtr",function(a,b){
    return a-b
})
// morgan is a http request logger middleware for nodejs
app.use(morgan('tiny'))


//set engine 
app.set('view engine', 'hbs');
app.engine('hbs',exhbs.engine({
    defaultLayout:'main.hbs',
    extname:'.hbs'
}))
// set view path 
app.set('views',path.join(__dirname+'/views'))
// import router
const router = require('./routes')
//use statistic file 
app.use(express.static(path.join(__dirname)+'/public/img'))
//use urlencoded because req.body do not have middleware
const bodyParser = require('body-parser')
const jsonParser = bodyParser.json()
const urlencodedParser = bodyParser.urlencoded({ extended: false })
app.use(express.json());
app.use(urlencodedParser)
router(app)
app.listen(port,()=>{
    console.log('listening on port 3000')
})
