# Pronom format map

Generates a JSON map of PRONOM formats to mimetypes by downloading a [DROID signature file](https://www.nationalarchives.gov.uk/aboutapps/pronom/droid-signature-files.htm) and pulling out the file formats.

Usage:

```
# fetches default (hard coded)
python make_pronom_map
```

```
# fetch specific file
python make_pronom_map https://cdn.nationalarchives.gov.uk/documents/DROID_SignatureFile_V108.xml
```

```
# write it out
python make_pronom_map > formats.json
```

## DDS (iiif-builder)

The DDS uses this map - drop an updated version here:

https://github.com/wellcomecollection/iiif-builder/blob/main/src/Wellcome.Dds/Wellcome.Dds.AssetDomain/Data/pronom_map.json
