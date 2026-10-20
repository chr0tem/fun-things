const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const EXTENSIONS = [".root", ".uid", ".nsc", ".pac", ".db", ".cfg", ".dat"];
const STORES = ["TES-SOU-04", "TES-LON-12", "TES-MAN-09", "TES-EDN-22"];

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function clearScreen() {
    console.clear();
    console.log("\x1b[32m==================================================");
    console.log("     ACUITAS ADVANCED DIAGNOSTIC UTILITY v2.4     ");
    console.log("==================================================\x1b[0m");
}

async function fastMatrixRain() {
    // This command updates the macOS terminal window title bar instantly!
    process.stdout.write("\x1b]2;user - fetchdata - 80x24\x07");

    console.log("\x1b[35m\n[INITIALISING DATA STREAM - DOWNLOADING REPOSITORIES]...\x1b[0m");
    console.log("\x1b[33mFetching Data... This should take about a minute.\x1b[0m\n");
    await sleep(2500);

    // Boosted to 1500 items. With a 40ms delay, it will take exactly 1 minute to finish!
    for (let i = 0; i < 1500; i++) {
        const randomStore = STORES[Math.floor(Math.random() * STORES.length)];
        const randomExt = EXTENSIONS[Math.floor(Math.random() * EXTENSIONS.length)];
        const randomNum = Math.floor(100000 + Math.random() * 900000);
        const size = (Math.random() * 12).toFixed(2);
        
        console.log(`\x1b[32mFETCHED: /sys/nodes/${randomStore}/data_${randomNum}${randomExt} (${size} MB) -> [SUCCESS]\x1b[0m`);
        await sleep(40); 
    }

    console.log("\n\x1b[33m✔ DOWNLOAD COMPLETE. 1500 DIRECTORY NODES SYNCHRONIZED.\x1b[0m");
    console.log("\x1b[32mSTATION STATUS: READY FOR ADMINISTRATIVE COMMANDS.\x1b[0m\n");
    
    console.log("Press any key to close this terminal window...");
    process.stdin.setRawMode(true);
    process.stdin.resume();
    process.stdin.on('data', () => process.exit(0));
}

function askPassword(ip, iid) {
    clearScreen();
    console.log(`\x1b[34mTARGET NODE: ${ip}\x1b[0m`);
    console.log(`\x1b[34mOPERATOR ID: ${iid}\x1b[0m\n`);
    
    rl.question("\x1b[36mENTER ROOT PASSWORD:\x1b[0m ", async (password) => {
        console.log("\x1b[33m\n[AUTHENTICATING ROOT CREDENTIALS]...\x1b[0m");
        await sleep(1200);
        
        console.log("\x1b[32m✔ ACCESS GRANTED. ROOT LEVEL ACCESS UNLOCKED.\x1b[0m");
        await sleep(600);
        
        await fastMatrixRain();
    });
}

function askIID(ip) {
    clearScreen();
    console.log(`\x1b[34mTARGET NODE: ${ip}\x1b[0m\n`);
    
    rl.question("\x1b[36mENTER 6-DIGIT STAFF ID CODE (e.g. 595937):\x1b[0m ", (iid) => {
        const trimmed = iid.trim();
        
        if (trimmed.startsWith("5959") && trimmed.length === 6 && !isNaN(trimmed)) {
            askPassword(ip, trimmed);
        } else {
            console.log("\n\x1b[31m⛔ [CONNECTION REFUSED]: INVALID OPERATOR STRUCTURE.\x1b[0m\n");
            setTimeout(() => askIID(ip), 1500);
        }
    });
}

function startTerminal() {
    clearScreen();
    rl.question("\x1b[36mENTER REMOTE TARGET IP ADDRESS (e.g. 192.168.1.45):\x1b[0m ", async (ip) => {
        console.log(`\x1b[33m\nPINGING ${ip.trim()}... RESPONSE RECEIVED IN 12ms.\x1b[0m`);
        await sleep(1000);
        askIID(ip.trim());
    });
}

startTerminal();
