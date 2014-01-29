var app;
app = angular.module("app", [])
.config(function($interpolateProvider) {
  /* $interpolateProvider 
   * we need replace {{ }} with  [[ ]]
   * */
  $interpolateProvider.startSymbol("[[");
  $interpolateProvider.endSymbol("]]");
})

app.controller('AppCtrl', [
  "$scope", 
  "$http", 
  function($scope, $http) {
  	var playload;

  	$scope.tweet_username = "";
  	$scope.tweet_text = "";
  	$scope.list_tweet = [];
    
    $scope.getTimeline = function () {
    	$http.get("/api/timeline")
    	.success(function (response) {
    		if (response.success) {
    			$scope.list_tweet = response.list_tweet;
    		} else {
    			$scope.alert = {};
    		}
    	})
    };

    $scope.writeTweet = function () {
    	playload = {
    		"username": $scope.tweet_username,
    		"text": $scope.tweet_text
    	};
    	$http.post("/api/timeline", playload)
    	.success(function (response) {
    		if (response.success) {
    			$scope.list_tweet = response.list_tweet;
    			$scope.tweet_username = "";
  				$scope.tweet_text = "";
    		} else {
    			$scope.alert = {};
    		}
    	})
    };

    $scope.removeTweet = function (index) {
    	$http.delete("/api/timeline/" + index + "/")
    	.success(function (response) {
    		if (response.success) {
    			$scope.list_tweet = response.list_tweet;
    		} else {
    			$scope.alert = {};
    		}
    	})
    };

    $scope.getTimeline();
  }
]);