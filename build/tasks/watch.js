'use strict';
var gulp = require('gulp');
var paths = require('../paths');


/**
 * Watch task
 * Run using "gulp watch"
 * Runs "watch-sass" and "watch-js" tasks
 */
gulp.task('watch', ['watch-sass', 'watch-js']);


/**
 * Watch-sass task
 * Run using "gulp watch-sass"
 * Runs "sass" task when any file in paths.sassSrc changes
 */
gulp.task('watch-sass', function() {
    gulp.watch(paths.sassSrc, ['sass']);
});


/**
 * Watch-js task
 * Run using "gulp watch-js"
 * Runs "js" and "lint" tasks when any file in paths.jsSrc changes
 */
gulp.task('watch-js', function() {
    gulp.watch([paths.jsSrc, paths.jsSpec], ['js', 'lint']);
});
