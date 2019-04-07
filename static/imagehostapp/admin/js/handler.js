var app=angular.module('IMG-HST',[]);


app.controller('IMG-CTR',function($scope,$http,$timeout){



$scope.signup_ng=function(){

	$http({
            method:"POST",
            url:"/save_user/",
            data:{
                'first_name':$scope.first_name,
                'last_name':$scope.last_name,
                'email':$scope.email,
                'password':$scope.password,
          
            }
        }).then(
        function (success){
           
            console.log(success.data);
            $scope.success=success.data.message;
            window.location='/login/'
            $scope.succ=true;
            alert("User data saved");
             $timeout(function(){
                $scope.succ=false;
            },10000);
            
            $scope.success="Details user Saved";

        },function(error){
            
            console.log(error.data);
            $scope.err=true;
            alert("not working");
            $timeout(function(){
                $scope.err=false;
            },10000);
            $scope.error=error.data;
            alert(error.data['message']);
        });

}



$scope.login_ng=function(){


	$http({

		method:"POST",
		url:'/login_check/',
		data:{
			'email':$scope.email,
			'password':$scope.password,
		}
	}).then(

			function(success){
			
			console.log(success.data);
			$scope.success=success.data.message;
			$scope.succ=true;
			alert("logged In");
			window.location='/upload_pic/'
			$timeout(function() {
				$scope.succ=false;
			}, 10000);

			},function(error){
			
			console.log(error.data);
			$scope.error=error.data.message;
			// alert("Its not working");
			$scope.err=true
			$timeout(function() {
				$scope.err=False;
			}, 10000);
			$scope.error=error.data;
			alert(error.data['message']);

			

			});

}


$scope.logout_ng=function(){


    $http({

        method:"POST",
        url:'/logout/',
        
    }).then(

            function(success){
            
            console.log(success.data);
            $scope.success=success.data.message;
            $scope.succ=true;
            alert("logged out");
            window.location='/'
            $timeout(function() {
                $scope.succ=false;
            }, 10000);

            },function(error){
            
            console.log(error.data);
            $scope.error=error.data.message;
            // alert("Its not working");
            $scope.err=true
            $timeout(function() {
                $scope.err=False;
            }, 10000);
            $scope.error=error.data;
            alert(error.data['message']);

            

            });

}










});



