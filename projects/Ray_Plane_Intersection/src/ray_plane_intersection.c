// Define the ray's origin and direction
vector rayOrigin = point(2, "P", 0);
vector rayDir = normalize( point(2, "P", 1)-point(2, "P", 0)); // Ensure the direction is normalized

// Define the plane's point and normal
vector planePoint = point(1, "P", 0);
vector planeNormal = point(1, "N", 0); // Assuming a horizontal plane

// Calculate the intersection
float denominator = dot(rayDir, planeNormal);

if (abs(denominator) > 1e-6) { // To avoid division by zero or parallel case
    vector p0MinusO = planePoint - rayOrigin;
    float t = dot(p0MinusO, planeNormal) / denominator;
    
    if (t >= 0) { // Intersection is in the direction of the ray
        vector intersectionPoint = rayOrigin + t * rayDir;
        // Do something with intersectionPoint, like printing it
        addpoint(0, intersectionPoint);
        printf("Intersection Point: %g %g %g\n", intersectionPoint.x, intersectionPoint.y, intersectionPoint.z);
    } else {
        printf("Intersection is behind the ray origin.\n");
    }
} else {
    printf("The ray is parallel to the plane.\n");
}
