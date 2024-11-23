import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Load words from the file
try:
    with open("english.txt", "r") as file:
        words = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    logger.error("The file 'english.txt' was not found. Make sure it exists in the script's directory.")
    words = []

# Define the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome! Use the /generate_word command to get a random word."
    )

# Define the /generate_word command
async def generate_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not words:
        await update.message.reply_text("No words available to generate. Please check the file.")
        return

    random_word = random.choice(words)
    await update.message.reply_text(f"Here is your random word: {random_word}")

# Main function to run the bot
def main() -> None:
    TOKEN = "7230166513:AAETVrbglM7dPqEhAK_la5h-X14vhpDtL50"  # Replace with your bot token

    application = ApplicationBuilder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("generate_word", generate_word))

    # Start the bot
    logger.info("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
