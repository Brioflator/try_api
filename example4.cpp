#include<vector>#include<algorithm>
typedef struct Block {
    int value;
    Block(int value): value(value) {}
} Block;

int main() {
    std::vector<Block> blocks;
    blocks.emplace_back(1);
    Block& block = blocks[0];
    blocks.emplace_back(2);
    std::max(1, block.value + 1);
    return 0;
}
