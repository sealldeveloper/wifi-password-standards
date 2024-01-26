# Wifi Password Defaults

Brute-Force Cracking Time hash rates used:
- M1: 40395 H/s
- [RTX 2060](https://gist.github.com/kennwhite/ad94dbb3a038d55d83286414598e1d93): 410.1 kH/s (410100 H/s)
- [RTX 4090](https://gist.github.com/Chick3nman/32e662a5bb63bc4f51b847bb422222fd): 2533.3 kH/s (2533300 H/s)

Calculated using: https://www.proxynova.com/tools/brute-force-calculator

Emojis mean:
- 🔴: Not able to be brute-forced
- 🟠: Depends on hardware/format
- 🟢: Brute-forcable

### 🟢 `WiFi-1234`
- Characters: 0-9
- Length: 8
- Example: 12345678
- Brute-Force Cracking Time (5x10^8 combos):
    - M1: 3h, 26m 
    - RTX 2060: 20m, 19s
    - RTX 4090: 3m, 4s
- Mask: `"?d?d?d?d?d?d?d?d"`

### 🟢 `NETGEAR00`
- Format: `noun` `adjective` `3 num`
- Example: zooyoung123
- Brute-Force Cracking Time (2.5x10^9 combos):
    - M1: 17h, 15m
    - RTX 2060: 1hr, 42m
    - RTX 4090: 16m, 30s

### 🟢 `MySpectrumWiFiA0`
- Format: `noun` `adjective` `3 num`
- Example: zooyoung123
- Brute-Force Cracking Time (2.5x10^9 combos):
    - M1: 17h, 15m
    - RTX 2060: 1hr, 42m
    - RTX 4090: 16m, 30s

### 🔴 `TelstraABC123`
- Characters: A-Z, 0-9
- Length: 10
- Example: A0B1C2D3E4
- Brute-Force Cracking Time (1.82x10^16 combos): Impossible with current technology
- Mask: `-1 "?d?u" "?1?1?1?1?1?1?1?1?1?1"`

### 🟢 `TelstraAB12`
- Characters: 0-9
- Length: 10
- Example: 1234567890
- Brute-Force Cracking Time (5x10^10 combos):
    - M1: 2w, 7h
    - RTX 2060: 1d, 9h
    - RTX 4090: 5h, 28m
- Mask: `"?d?d?d?d?d?d?d?d?d?d"`

### 🔴 `OPTUSVDABCD123`
- Format: `noun (5char upper)` `noun (5char upper)` `5 num/a-Z`
- Example: HORSESTUFF12345
- Brute-Force Cracking Time (5.74x10^14 combos): Impossible with current technology

### 🟠 `OPTUS_ABC123`
- Format: `noun (5char lower)` `noun (5char lower)` `5 num/a-Z`
- Example: cakeyflimp12345
- Brute-Force Cracking Time (5.74x10^14 combos): Impossible with current technology

OR 

- Format: `noun (5char lower)` `5 nums` `2 a-z`
- Example: cakey12345aa
- Brute-Force Cracking Time (7.41x10^12 combos):
    - M1: 5y, 9M
    - RTX 2060: 6M, 3w
    - RTX 4090: 1M, 3d

### 🔴 `Optus-4G-AB12-CD34`
- Characters: A-Z, 0-9
- Length: 11
- Example: 1A2B3C4D5E6
- Brute-Force Cracking Time (6.58x10^17 combos): Impossible with current technology
- Mask: `-1 "?d?u" "?1?1?1?1?1?1?1?1?1?1?1"`

## 🔴 `DODO-ABCD`
- Characters: A-Z, 0-9
- Length: 10
- Example: 1A2B3C4D5E
- Brute-Force Cracking Time (1.82x10^16 combos): Impossible with current technology
- Mask: `-1 "?d?u" "?1?1?1?1?1?1?1?1?1?1"`

## 🔴 `DODOABCD`
- Characters: A-Z, 0-9
- Length: 9
- Example: 1A2B3C4D5
- Brute-Force Cracking Time (5.07x10^14 combos): Impossible with current technology
- Mask: `-1 "?d?u" "?1?1?1?1?1?1?1?1?1"`

## 🔴 `NetComm 1234`
- Format: 1st a-Z, 9 a-z
- Brute-Force Cracking Time (1.41x10^15 combos): Impossible with current technology
- Mask: `-1 "?u?l" "?1?l?l?l?l?l?l?l?l?l"`

## 🔴 `WiFi-A1B2C3`
- Characters: a-Z, 0-9
- Length: 16
- Brute-Force Cracking Time (8.72x10^22 combos): Impossible with current technology
- Mask: `-1 "?u?l?d" "?1?1?1?1?1?1?1?1?1?1?1?1?1?1?1?1"`

## 🔴 `VX220-A1B2`
- Characters: A-Z, 0-9
- Length: 13
- Notes: Seem to always start with `32`
- Brute-Force Cracking Time (assuming they start with 32) (6.58x10^17 combos): Impossible with current technology
- Mask: `-1 "?u?d" "?1?1?1?1?1?1?1?1?1?1?1"` or `-1 "?u?d" -2 "3" -3 "2" "?2?3?1?1?1?1?1?1?1?1?1"`

## 🔴 `HUAWEI-A1B2-C3D4`
- Characters: A-Z, 0-9
- Length: 11
- Brute-Force Cracking Time (6.58x10^17 combos): Impossible with current technology
- Mask: `-1 "?d?u" "?1?1?1?1?1?1?1?1?1?1?1"`

## 🟢 `TP-Link_A1B2`
- Characters: 0-9
- Length: 8
- Brute-Force Cracking Time (5x10^8 combos):
    - M1: 3h, 26m 
    - RTX 2060: 20m, 19s
    - RTX 4090: 3m, 4s
- Mask: `"?d?d?d?d?d?d?d?d"`

## 🔴 `BelongA1B2C3`
- Characters: a-z, 0-9
- Length: 12
- Brute-Force Cracking Time (5.24x10^18 combos): Impossible with current technology
- Mask: `-1 "?d?l" "?1?1?1?1?1?1?1?1?1?1?1?1"`
