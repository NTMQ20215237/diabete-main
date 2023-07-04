const  controllers = require('../app/controller/home')
function router (app){
    app.get('/detail',controllers.homePost) //for tesing purpose
    app.post('/',controllers.homePost)
    app.get('/',controllers.home)
}

module.exports= router
