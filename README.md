# Email a Notion Database

This python script allows to collect rows from a Notion database and send it to an email address.


# Example usage

```bash
# Install the library using pip
python -m pip install git+https://github.com/agonzalezl/email-notion-database.git
python3 -m email_notion_database.main \
        --token '<notion_token>' \
        --email-server 'smtp.gmail.com' \
        --email-port 465 \
        --sender-address '<your_email>'\
        --sender-name '<your_name>' \
        --sender-password '<your_email_pass>'  \
        --subject '<email_subject>' \
        --target-address 'taget_email_address' \
        --email-title 'email_title' \
        --email-header 'email_header_text' \
        --number-rows 'notion_rows_to_send' \
        --notion-filter-json  '{"property":"Done","checkbox":{"equals":true}}' \
        --notion-db-id 'notion_db_id'
```

## Give your Notion Integration token access to your page
After creating a token in [my-integrations](https://www.notion.so/my-integrations), in your Notion page click `Share`, click in the `invite` search box and search for the name of your integration.

# Acknowledgements

Thanks to Notion for continuing to make cool stuff 💜
