// Linear interpolation function
float custom_lerp(float a; float b; float t) {
    return a + t * (b - a);
}

// Fade function using the improved Perlin fade curve
float fade(float t) {
    return t * t * t * (t * (t * 6 - 15) + 10);
}

// Hash function to generate a unique float based on seed
float hash(float n) {
    float frac = sin(n) * 47999999988;
    return frac - int(frac);
}

// Gradient function to calculate dot product based on hash
float grad(float hash; float x) {
    int h = int(hash * 15.0) % 16;
    float grad = 1.0 - (h % 8) / 7.0 * (h < 8 ? 1.0 : -1.0);
    return (grad * x);
}

// 1D Perlin noise function
float perlin(float x) {
    float X = floor(x);
    x = x - X;
    float x0 = x - 0.0;
    float x1 = x - 1.0;

    float n0 = grad(hash(X), x0);
    float n1 = grad(hash(X + 1.0), x1);

    return custom_lerp(n0, n1, fade(x));
}
vector pos = @P;
@P = set(perlin(pos.x), perlin(pos.y), perlin(pos.z));
