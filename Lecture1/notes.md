We have some function f(x) which represents input data x, weights w, bias b, predicitons y.
This function itself is complex one and represents the perceptron. In its essense it is just:
w*x + b = y (the formula of the line, but as we said, in reality it is more complex).
We now go through learning phase, where we need to figure out w and b values.
We first compute derivatives for w and b with respect to the y. They are called "gradients".
It is the same as the slope to the function. If the gradient is negative it means, that the function is decreasing in that point,
if the gradient is positive it means, that the function is increasing in that point. The 0 gradient is the critical point of the function,
where it changes its direction.
At this point, we initialized w and b to any random values and computed gradients.
Now we can use some test input data x and calculate y. After, we will compare y pred with y ground truth and will calculate the loss.
And our function becomes this:
loss = ((y_pred - - y_truth)**2 * w + b)
I guess here we want to calculate gradients with respect to the loss.
Once we have gradients, we know that gradient points to the steepest increase of the functiom.
We want to decrease loss, therefore we want to change w and b in the oposite direction of their gradients.