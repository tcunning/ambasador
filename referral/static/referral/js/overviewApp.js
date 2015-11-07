var overviewApp = angular.module('overviewApp', []);

// Allow Django to use {{ xyz }} variables and a
// Allow angular to use {[{ xyz }]} variables 
overviewApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
 
// MARK 2

overviewApp.controller('ReferralListController', ['$scope', '$window', function($scope, $window) {
    var referralList = this;
    
    referralList.referrals = $window.initialReferrals;
    //
    //referralList.initialReferralRemaining = function() {
    //   return referralList.initialReferral.count;
    //};    
    
    //referralList.todos = [
    //    {text:'learn angular', done:true},
    //    {text:'build an angular app', done:false}];

    referralList.addReferral = function() {
        referralList.referrals.push({name:referralList.referralText, count:0});
        referralList.referralText = '';
    };

    referralList.removeReferral = function(referral) {
        var referralIndex = referralList.referrals.indexOf(referral)
        referralList.referrals.splice(referralIndex,1)
    };


    //referralList.remaining = function() {    
    //   var count = 0;
    //   angular.forEach(referralList.todos, function(todo) {
    //      count += todo.done ? 0 : 1;
    //   });
    //   return count;
    //};

    //referralList.archive = function() {
    //   var oldTodos = referralList.todos;
    //   referralList.todos = [];
    //   angular.forEach(oldTodos, function(todo) {
    //      if (!todo.done) referralList.todos.push(todo);
    //   });
    //};
}]);

