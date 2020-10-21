CCLI = CCLI='${HOME}/.local/bin/cardano-cli'
# CCLI=os.path.expanduser("~") + '/.local/bin/cardano-cli'  # Override automatic detection of path to cardano-cli executable
# CNODE_HOME="${HOME}/cardano-node"                       # Override default CNODE_HOME path (defaults to /opt/cardano/cnode)
# CNODE_PORT=3000                                         # Set node port
# CONFIG="${CNODE_HOME}/config/config.json"               # Override automatic detection of node config path
# SOCKET="${CNODE_HOME}/db/node.socket"                   # Override automatic detection of path to socket
# EKG_HOST=127.0.0.1                                     # Set node EKG host
# EKG_PORT=12788                                         # Override automatic detection of node EKG port
# EKG_TIMEOUT=3                                          # Maximum time in seconds that you allow EKG request to take before aborting (node metrics)
# BLOCK_LOG_DIR="${CNODE_HOME}/db/blocks"                # CNTools Block Collector block dir set in cntools.config, override path if enabled and using non standard path
CURL_TIMEOUT=10                                        # Maximum time in seconds that you allow curl file download to take before aborting (GitHub update process)


# TMP_FOLDER="/tmp/cntools"
# TIMEOUT_NO_OF_SLOTS=60 # used when waiting for a new block to be created

# TIMEOUT_LEDGER_STATE=300 # used for querying ledger-state

# output verbosity
# 0 = Minimal - Show relevant information
# 1 = Normal  - More information about whats going on behind the scene
# 2 = Maximal - Debug level for troubleshooting
# VERBOSITY=0

# a file to know the last hardfork transition by grepping the logs
# SHELLEY_TRANS_FILENAME="$CNODE_HOME/db/shelley_trans_epoch"

# each wallet and pool has a friendly name and subfolder containing all related keys, certificates, ...
# WALLET_FOLDER="$CNODE_HOME/priv/wallet"
# POOL_FOLDER="$CNODE_HOME/priv/pool"

# standardized names for all wallet/pool related files
WALLET_PAY_VK_FILENAME="payment.vkey"
WALLET_PAY_SK_FILENAME="payment.skey"
WALLET_PAY_ADDR_FILENAME="payment.addr"
WALLET_BASE_ADDR_FILENAME="base.addr"
WALLET_STAKE_VK_FILENAME="stake.vkey"
WALLET_STAKE_SK_FILENAME="stake.skey"
WALLET_STAKE_ADDR_FILENAME="reward.addr"
WALLET_STAKE_CERT_FILENAME="stake.cert"
WALLET_DELEGCERT_FILENAME="delegation.cert"
POOL_ID_FILENAME="pool.id"
POOL_HOTKEY_VK_FILENAME="hot.vkey"
POOL_HOTKEY_SK_FILENAME="hot.skey"
POOL_COLDKEY_VK_FILENAME="cold.vkey"
POOL_COLDKEY_SK_FILENAME="cold.skey"
POOL_OPCERT_COUNTER_FILENAME="cold.counter"
POOL_OPCERT_FILENAME="op.cert"
POOL_VRF_VK_FILENAME="vrf.vkey"
POOL_VRF_SK_FILENAME="vrf.skey"
POOL_CONFIG_FILENAME="pool.config"
POOL_REGCERT_FILENAME="pool.cert"
POOL_CURRENT_KES_START="kes.start"
POOL_DEREGCERT_FILENAME="pool.dereg"

# kes rotation warning (in seconds)
KES_ALERT_PERIOD=172800 # default 2 days
KES_WARNING_PERIOD=604800 # default 7 days

# limit for extended wallet selection menu filtering (balance check and delegation status)
# if more wallets exist than limit set these checks will be disabled to improve performance
WALLET_SELECTION_FILTER_LIMIT=10

# log cntools activities (comment out to disable)
# CNTOOLS_LOG="${CNODE_HOME}/logs/cntools-history.log"