#!/bin/bash

# Initialize handheld memory banks
BATTERY=100
TOKENS=20
CRYSTALS=0
CURRENT_SCREEN="HOME"
THEME="BLUE"

# Setup visual ANSI colors
RESET="\x1b[0m"
BOLD="\x1b[1m"
BLUE_TAG="\x1b[36m"
GREEN_TAG="\x1b[32m"
PURPLE_TAG="\x1b[35m"
YELLOW_TAG="\x1b[33m"
WHITE_TAG="\x1b[37m"
RED_TAG="\x1b[31m"

cleanup() {
    tput cnorm # Restore cursor
    clear
    echo -e "${RESET}MePhone OS shell powered off safely."
    exit 0
}
trap cleanup SIGINT

while true; do
    # WIPE THE WHOLE WINDOW CLEAN FIRST
    clear
    tput civis # Hide the blinking terminal cursor

    COLS=$(tput cols)
    ROWS=$(tput lines)
    MID_Y=$((ROWS / 2))

    # Slowly reduce battery level
    if [ $((RANDOM % 40)) -eq 0 ] && [ $BATTERY -gt 1 ]; then
        BATTERY=$((BATTERY - 1))
    fi

    # Choose header tag styles dynamically based on active settings
    case $THEME in
        "GREEN") ACTIVE_COLOR=$GREEN_TAG; TAG="📟 [ MATRIX_NODE ]" ;;
        "PURPLE") ACTIVE_COLOR=$PURPLE_TAG; TAG="👾 [ CORETX_NET ]" ;;
        *) ACTIVE_COLOR=$BLUE_TAG; TAG="📱 [ MePhone 5.0 ]" ;;
    esac

    # 1. Print Status Bar
    TIME_STR=$(date +"%H:%M:%S")
    echo -e "${WHITE_TAG}${TAG}${RESET}  📶 Tesco-Net  ${GREEN_TAG}🔋 ${BATTERY}%${RESET}  ${YELLOW_TAG}💰 ${TOKENS}T${RESET}  ${ACTIVE_COLOR}⏰ ${TIME_STR}${RESET}"
    
    # 2. Print Separator Row
    move_line=""
    for ((x=0; x<COLS; x++)); do move_line+="-"; done
    echo -e "${WHITE_TAG}${move_line}${RESET}"

    # Pad top spacing down to center area
    for ((i=0; i<MID_Y-5; i++)); do echo ""; done

    # 3. DRAW APP CANVAS LABELS
    if [ "$CURRENT_SCREEN" = "HOME" ]; then
        printf "%$(( (COLS - 26) / 2 ))s${BOLD}${ACTIVE_COLOR}🔥 MEPHONE OS LAUNCHPAD 🔥${RESET}\n\n" " "
        printf "%$(( (COLS - 32) / 2 ))s [1] Launch Calculator Engine\n" " "
        printf "%$(( (COLS - 32) / 2 ))s [2] Open Cosmic Miner Game\n" " "
        printf "%$(( (COLS - 32) / 2 ))s [3] Load System Settings Suite\n\n" " "
        printf "%$(( (COLS - 32) / 2 ))sPress [Q] key to Power Down Phone\n" " "

    elif [ "$CURRENT_SCREEN" = "MINER" ]; then
        printf "%$(( (COLS - 24) / 2 ))s${BOLD}${YELLOW_TAG}🪐 COSMIC ASTEROID MINER${RESET}\n\n" " "
        echo -e "    💎 Collected Shards: ${GREEN_TAG}${CRYSTALS}${RESET}"
        echo -e "    💰 Wallet Balance:  ${YELLOW_TAG}${TOKENS}${RESET} Space-Tokens\n"
        echo -e "    👉 按 [M] 键 ⛏️ 采掘矿石 (65% 几率获得晶体 & 15代币)"
        echo -e "    👉 按 [B] 键 🛒 消耗 40 代币充能动力电池组至 100%"

    elif [ "$CURRENT_SCREEN" = "CALC" ]; then
        printf "%$(( (COLS - 25) / 2 ))s${BOLD}${BLUE_TAG}🧮 INTEGRATED MATH REGISTERS${RESET}\n\n" " "
        echo -e "      Register A Cache: 59"
        echo -e "      Register B Cache: 45\n"
        echo -e "      Computed Accumulator Sum: ${GREEN_TAG}104${RESET}"

    elif [ "$CURRENT_SCREEN" = "SETTINGS" ]; then
        printf "%$(( (COLS - 25) / 2 ))s${BOLD}${PURPLE_TAG}⚙️ SYSTEM CONFIG CONTROL PANEL${RESET}\n\n" " "
        echo -e "      Hardware Code: 5959-3745-MEPHONE"
        echo -e "      Tesco Link:   Station 04 Online\n"
        echo -e "      🎨 THEME CONTROLLER SKINS:"
        echo -e "      按 [B] 键切换 - Classic Blue Aesthetic"
        echo -e "      按 [G] 键切换 - Matrix Digital Green"
        echo -e "      按 [P] 键切换 - Cyberpunk Hacker Purple"
    fi

    # Pad bottom spacing down to the footer
    for ((i=0; i<MID_Y-4; i++)); do echo ""; done

    # 4. DRAW BOTTOM HOME PANEL FOOTER ROW
    home_bar="[========= ( 🔘 敲键盘 'H' 键返回 HOME 主界面 ) =========]"
    printf "%$(( (COLS - ${#home_bar}) / 2 ))s%s\n" " " "${home_bar}"

    # 5. FIXED KEYBOARD SCANNER: Set to a valid 1-second timeout loop
    if read -s -n 1 -t 1 key_in; then
        CHAR=$(echo "$key_in" | tr '[:lower:]' '[:upper:]')
        
        if [ "$CHAR" = "H" ]; then
            CURRENT_SCREEN="HOME"
        elif [ "$CURRENT_SCREEN" = "HOME" ]; then
            if [ "$CHAR" = "1" ]; then CURRENT_SCREEN="CALC";
            elif [ "$CHAR" = "2" ]; then CURRENT_SCREEN="MINER";
            elif [ "$CHAR" = "3" ]; then CURRENT_SCREEN="SETTINGS";
            elif [ "$CHAR" = "Q" ]; then cleanup; fi
        elif [ "$CURRENT_SCREEN" = "MINER" ]; then
            if [ "$CHAR" = "M" ]; then
                if [ $((RANDOM % 100)) -lt 65 ]; then
                    CRYSTALS=$((CRYSTALS + 1))
                    TOKENS=$((TOKENS + 15))
                fi
            elif [ "$CHAR" = "B" ] && [ $TOKENS -ge 40 ]; then
                TOKENS=$((TOKENS - 40))
                BATTERY=100
            fi
        elif [ "$CURRENT_SCREEN" = "SETTINGS" ]; then
            if [ "$CHAR" = "B" ]; then THEME="BLUE";
            elif [ "$CHAR" = "G" ]; then THEME="GREEN";
            elif [ "$CHAR" = "P" ]; then THEME="PURPLE"; fi
        fi
    fi
done
