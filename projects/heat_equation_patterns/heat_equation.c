// Parameters
float alpha = 1; // Thermal diffusivity, adjust based on your needs
float dt = 7.0; // Time step, adjust based on your simulation requirements
float laplacian;
int neighbors[];
int numNeighbors;
float tempSum;
float currentTemp;
float newTemp;

// Iterate over all points in the geometry
for (int pt = 0; pt < npoints(0); ++pt) {
    laplacian = 0.0;
    neighbors = neighbours(0, pt);
    numNeighbors = len(neighbors);
    tempSum = 0.0;
    // Iterate over the neighbors of the curren  point
    for (int i = 0; i < numNeighbors; ++i) {
        tempSum += point(0, "temp", neighbors[i]);
    }
    currentTemp = 0;
    if (numNeighbors > 0) {
        float avgTemp = tempSum / numNeighbors;
        currentTemp = point(0, "temp", pt);
        laplacian = avgTemp - currentTemp;
    }
    // Update the temperature of the current point
    newTemp = currentTemp + dt * alpha * laplacian;
    setpointattrib(0, "temp", pt, newTemp, "set");
}