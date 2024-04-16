
# Marching Cubes implementation technical docs

## Edge Table

The [edgeTable](https://github.com/mrnsapple/HoudiniTips/projects/MarchingCubes/src/marching_cuves_vex.c#L8) consists of 256 entries, each representing one of the possible combinations of vertices above or below the isosurface (since each of the 8 vertices of a cube can either be above or below the threshold, there are 2^8 = 256 combinations). Each entry is a 12-bit number where each bit corresponds to an edge of the cube (there are 12 edges on a standard cube).

## Triangle Table

The [triTable](https://github.com/mrnsapple/HoudiniTips/projects/MarchingCubes/src/marching_cuves_vex.c#L41) provides the triangulation pattern based on the cube index. Each entry corresponds to one of the entries in the edgeTable and contains up to 15 values, which represent the edges forming the triangles. Each group of three numbers forms one triangle. The table can have up to 5 triangles for any cube configuration.

## Interpolation

The [following example](https://github.com/mrnsapple/HoudiniTips/projects/MarchingCubes/src/marching_cuves_vex.c#L354) provides the VEX syntax to interpolate the vertex positions where the isosurface intersects the edges of a cube. Each edge connects two vertices, and you perform interpolation if the isosurface passes between them.

### Explanation
Each if statement checks a specific bit in the edges variable. Each bit corresponds to one of the cube's 12 edges. The bits are checked using the bitwise AND operator &.
The interpolate function is called with the positions and values of the endpoints of each edge. This function computes the point of intersection along the edge where the isosurface passes through, based on the isoLevel.

### Implementation Notes

edges Calculation: Ensure that the edges variable correctly reflects the bit pattern based on which cube edges are intersected by the isosurface. This requires setting up the initial cubeIndex correctly and using the edgeTable lookup.
interpolate Function: Make sure this function correctly implements the linear interpolation formula, as previously outlined.
This approach effectively calculates the vertices of the mesh where the isosurface intersects the cube, enabling you to construct triangles in the subsequent steps.

### Bitshifting and cubeIndex explanation

In the context of the Marching Cubes algorithm, [cubeIndex](https://github.com/mrnsapple/HoudiniTips/projects/MarchingCubes/src/marching_cuves_vex.c#L334) is used to represent the state of the cube's corners regarding whether they are inside or outside of the isosurface (a surface that represents points of a constant value within a volume of space). Each bit in cubeIndex corresponds to one of the cube's corners:

The 0th bit represents the first corner,
The 1st bit represents the second corner, and so on.
If a corner is inside the isosurface, the corresponding bit in cubeIndex is set to 1. The line cubeIndex |= 1 << i; is executed if the i-th corner of the cube is inside the isosurface. This operation effectively sets the i-th bit of cubeIndex to 1 without affecting the other bits.

Example:
Assume we are processing a cube and determining which of its corners are inside the isosurface. If the 0th, 2nd, and 3rd corners are inside, the following operations would occur sequentially:

Initially, cubeIndex is 0 (binary 00000000).
If the 0th corner is inside, cubeIndex |= 1 << 0; sets the 0th bit: cubeIndex becomes 00000001.
If the 2nd corner is inside, cubeIndex |= 1 << 2; sets the 2nd bit: cubeIndex becomes 00000101.
If the 3rd corner is inside, cubeIndex |= 1 << 3; sets the 3rd bit: cubeIndex becomes 00001101.
This process builds up a binary number where each set bit indicates a corner of the cube that is inside the isosurface. This binary number (or cubeIndex) can then be used to look up how to triangulate the cube based on which of its corners are inside the isosurface.

For vex instead of cubeIndex |= 1 << 0, we use [cubeIndex |= int(1 * pow(2, i))](https://github.com/mrnsapple/HoudiniTips/projects/MarchingCubes/src/marching_cuves_vex.c#L339).Because VEX does not support the << (left shift) and >> (right shift) operators directly for shifting bits.

pow(2, i) computes 2 raised to the power of i, which is equivalent to shifting 1 left by i positions in bit manipulation terms.

The int() cast ensures that the result is treated as an integer, suitable for bitwise operations.
cubeIndex |= int(1 * pow(2, i)); effectively sets the i-th bit of cubeIndex if the condition is true, mimicking the bit shifting operation.
