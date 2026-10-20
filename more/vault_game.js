const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function clearScreen() {
    console.clear();
    console.log("\x1b[35m==================================================");
    console.log("       SECURE INDUSTRIAL VAULT SYSTEMS v1.0b      ");
    console.log("==================================================\x1b[0m");
}

function askPassword() {
    clearScreen();
    console.log("\n🔒 \x1b[31m[STATUS: LOCKED]\x1b[0m The heavy steel safe doors are shut tight.");
    
    rl.question("\n\x1b[36mENTER 4-DIGIT COMBINATION CODE:\x1b[0m ", (guess) => {
        const trimmed = guess.trim();

        // Check if the guess matches your master password rule
        if (trimmed === "4386") {
            clearScreen();
            console.log("\n🔓 \x1b[32m[STATUS: OPENED]\x1b[0m");
            console.log("\x1b[32m*CLANG-CLANG-CLANG!*\x1b[0m");
            console.log("\n✨ \x1b[36mACCESS GRANTED! The locking bars slide back dynamically.\x1b[0m");
            console.log("\x1b[32mYou successfully cracked the safe!\x1b[0m\n");
            rl.close();
        } else {
            console.log("\n❌ \x1b[31m[ACCESS DENIED]: CODE MISMATCH.\x1b[0m");
            console.log("The terminal emits a sharp error tone. Try again...\n");
            
            // Wait 1.5 seconds so they can read the error before resetting the screen
            setTimeout(askPassword, 1500);
        }
    });
}

// Boot up the JavaScript engine
askPassword();
