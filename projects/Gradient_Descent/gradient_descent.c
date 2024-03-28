// Assume `@P` is the point's position
// Parameters for the "spiral target"
float angle = ch("angle");
float radius = ch("radius");
float angleIncrement = ch("angleIncrement"); // How fast we rotate around
float radiusIncrement = ch("radiusIncrement"); // How fast we move outward

// Gradient Descent parameters
float learningRate = ch("learningRate");
int iterations = chi("iterations");

//@identifier = @ptnum;

for (int i = 0; i < iterations; ++i)
{
    // Calculate the current target position on the spiral
    vector targetPos = set(radius * cos(angle), radius * sin(angle), 0);
    
    // Define the gradient of the squared distance function with respect to the point's position
    vector gradient = 2 * (@P - targetPos);
    
    // Update the point's position using gradient descent
    @P -= learningRate * gradient;
    
    // Move the target along the spiral
    angle += angleIncrement;
    radius += radiusIncrement;
    //Create Points to track gradient
    int pointNum = addpoint(0, @P);
    setpointattrib(0, "identifier", pointNum, @ptnum); 
}
