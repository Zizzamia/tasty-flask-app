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
  "$timeout",
  function($scope, $http, $timeout) {
  	var playload;

  	$scope.tweet_username = "";
  	$scope.tweet_text = "";
  	$scope.list_tweet = [];
    $scope.seconds_to_refresh = 5;
    
    $scope.getTimeline = function () {
    	$http.get(path + "/api/timeline")
    	.success(function (response) {
    		if (response.success) {
    			$scope.list_tweet = response.list_tweet;
          $scope.seconds_to_restart = response.seconds_to_restart;
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
    	$http.post(path + "/api/timeline", playload)
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
    	$http.delete(path + "/api/timeline/" + index + "/")
    	.success(function (response) {
    		if (response.success) {
    			$scope.list_tweet = response.list_tweet;
    		} else {
    			$scope.alert = {};
    		}
    	})
    };

    $scope.restartTimeline = function () {
      $http.get(path + "/api/timeline/restart/")
      .success(function (response) {
        if (response.success) {
          $scope.list_tweet = response.list_tweet;
          $scope.seconds_to_restart = response.seconds_to_restart;
        } else {
          $scope.alert = {};
        }
      })
    };

    (function tick() {
        $scope.seconds_to_refresh -= 1;
        $scope.seconds_to_restart -= 1;
        if ($scope.seconds_to_refresh <= 0) {
          $scope.seconds_to_refresh = 5;
          $scope.getTimeline();
        }
        if ($scope.seconds_to_restart <= 0) {
          $scope.restartTimeline();
        }
        $timeout(tick, 1000);
    })();

    $scope.getTimeline();
  }
]);