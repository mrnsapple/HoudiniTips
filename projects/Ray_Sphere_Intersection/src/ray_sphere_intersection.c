// Define the ray
vector rayOrigin = point(2, "P", 0);
vector rayDir = normalize( point(2, "P", 1)-point(2, "P", 0)); // Ensure the direction is normalized

// Define the sphere
vector sphereCenter = chv("../sphere2/t");// {5, 5, 5}; // Sphere center
float radius = chf("../sphere2/scale"); // Sphere radius

// Calculate the components of the quadratic equation
vector oc = rayOrigin - sphereCenter;
float A = dot(rayDir, rayDir);
float B = 2 * dot(oc, rayDir);
float C = dot(oc, oc) - radius * radius;

// Solve the quadratic equation
float discriminant = B*B - 4*A*C;

if (discriminant > 0) {
    // Two intersections
    float t1 = (-B - sqrt(discriminant)) / (2*A);
    float t2 = (-B + sqrt(discriminant)) / (2*A);

    // Use the smallest positive t to find the closest intersection point
    float t = t1 < t2 && t1 > 0 ? t1 : t2;
    if (t > 0) {
        vector intersectionPoint = rayOrigin + t * rayDir;
        addpoint(0, intersectionPoint);
        printf("Intersection Point: %g %g %g\n", intersectionPoint.x, intersectionPoint.y, intersectionPoint.z);
    } else {
        printf("Intersection is behind the ray origin.\n");
    }
} else if (discriminant == 0) {
    // One intersection, tangent to sphere
    float t = -B / (2*A);
    vector intersectionPoint = rayOrigin + t * rayDir;
    printf("Tangent Point: %g %g %g\n", intersectionPoint.x, intersectionPoint.y, intersectionPoint.z);
} else {
    // No intersection
    printf("No intersection.\n");
}
