import re

class SimpleSmartContractGenerator:
    def __init__(self):
        self.templates = {
            'token': self.generate_token_contract,
            'crowdsale': self.generate_crowdsale_contract,
        }

    def generate_contract(self, description):
        for keyword, generator in self.templates.items():
            if re.search(keyword, description, re.IGNORECASE):
                return generator(description)
        return "Sorry, no matching contract template found."

    def generate_token_contract(self, description):
        return """
        pragma solidity ^0.8.0;

        contract SimpleToken {
            string public name = "SimpleToken";
            string public symbol = "STKN";
            uint8 public decimals = 18;
            uint256 public totalSupply = 1000000 * (10 ** uint256(decimals));
            mapping(address => uint256) public balanceOf;

            constructor() {
                balanceOf[msg.sender] = totalSupply;
            }

            function transfer(address to, uint256 value) public returns (bool success) {
                require(balanceOf[msg.sender] >= value, "Insufficient balance.");
                balanceOf[msg.sender] -= value;
                balanceOf[to] += value;
                return true;
            }
        }
        """

    def generate_crowdsale_contract(self, description):
        return """
        pragma solidity ^0.8.0;

        contract SimpleCrowdsale {
            address public owner;
            uint256 public rate = 1000; // tokens per ether
            mapping(address => uint256) public balanceOf;

            constructor() {
                owner = msg.sender;
            }

            receive() external payable {
                uint256 tokens = msg.value * rate;
                balanceOf[msg.sender] += tokens;
            }

            function withdraw() public {
                require(msg.sender == owner, "Only owner can withdraw.");
                payable(owner).transfer(address(this).balance);
            }
        }
        """
