# Code Crucible Anvil

## Anvil

Anvil is the AI brains of CCDE (Code Crucible Development Environment). Anvil is responsible for creating prompts, communicating with LLMs, and coordinating everything needed to power the AI features in the editor.

Anvil is a fork of the original "Sidecar" project by CodeStory AI, which was the AI engine for their now sunset "Aide" editor. While the original editor was sunset, we've created a fork of both the editor (now CCDE) and its AI engine (now Anvil) to continue development with a focus on privacy and offline capabilities.

Broadly speaking these are the following important components in Anvil:
- `tool_box.rs` - The collection of all and any tools AI might need is present here, all the language specific smartness is handled by `tool_box.rs`
- `symbol/` - The symbol folder contains the code which allows each individual symbol to be smart and independent. This can work on any granularity level, all the way from a file to a single function or function inside a class (its very versatile)
- `llm_prompts/` - This contains the prompt templates used for various AI interactions in the editor
- `repomap` - This creates a repository map using page rank on the code symbols. Most of the code here is a port of the python implementation done on Aider

## Project Status

This project is a fork of the original Sidecar codebase that powered Aide. While the original Aide editor was sunset by CodeStory AI, we're reviving both the editor (as CCDE) and its AI engine (as Anvil) as part of the Code Crucible project. Our focus is on:

1. Rebranding from Sidecar to Anvil
2. Implementing privacy-first architecture by removing cloud dependencies


## Getting Started
1. Ensure you are using Rust 1.73
2. Build the binary: `cargo build --bin webserver`
3. Run the binary: `./target/debug/webserver`

## Using Anvil with CCDE:
1. Run the Ccde production build or build from source using [this](https://github.com/codecruciblecc/ccde)
2. Run the Anvil binary
3. Since you have an Anvil binary already running, the editor will prefer to use this over starting its own process
4. You are now running Anvil for CCDE locally with your own built binary

## Contributing

There are many ways in which you can participate in this project, for example:

* [Submit bugs and feature requests](https://github.com/codecruciblecc/anvil/issues), and help us verify as they are checked in
* Review [source code changes](https://github.com/codecruciblecc/anvil/pulls)

If you are interested in fixing issues and contributing directly to the code base,
please see the document [How to Contribute](HOW_TO_CONTRIBUTE.md), which covers the following:

* [How to build and run from source](HOW_TO_CONTRIBUTE.md)
* [The development workflow, including debugging and running tests](HOW_TO_CONTRIBUTE.md#debugging)
* [Submitting pull requests](HOW_TO_CONTRIBUTE.md#pull-requests)

## Feedback

* [File an issue](https://github.com/codecruciblecc/anvil/issues)
* [Request a new feature](CONTRIBUTING.md)
* Upvote [popular feature requests](https://github.com/codecruciblecc/anvil/issues?q=is%3Aopen+is%3Aissue+label%3Afeature-request+sort%3Areactions-%2B1-desc)

## Code of Conduct

This project has adopted the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). Please read the Code of Conduct before contributing to this project.

## Acknowledgements

We would like to acknowledge the original project's creation by CodeStory AI for their initial work and vision. 

## License

Original work Copyright (c) 2024 CodeStory AI.
Modified work Copyright (c) 2024 CodeCrucible AI. All rights reserved.
Licensed under the [GNU Affero General Public License v3.0](LICENSE.md).