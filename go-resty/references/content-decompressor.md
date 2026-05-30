---
weight: 7
---

# Content Decompressor

Resty v3 provides an extensible way to handle Response content decompression. Out-of-the-box, it handles `gzip` and `deflate` decompress.

> [!NOTE]
> **NOTE:**
> * User-defined decompressor takes priority over default ones.
> * Add method overwrites decompressor if `decompress` directive/key already exists.
> * [Content-Encoding directive/key](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding) is important while adding decompressor.

## Example

Refer to the example section for [Brotli (br)]({{% relref "decompress-brotli" %}}) and [Zstandard (zstd)]({{% relref "decompress-zstandard" %}}) decompress.

```go
c := resty.New()
defer c.Close()

c.AddContentDecompressor("decompress directive/key here", func(r io.ReadCloser) (io.ReadCloser, error) {
    // logic goes here

    return nil, nil
})
```

## Methods

* [Client.AddContentDecompressor]({{% godoc v3 %}}Client.AddContentDecompressor)
* [Client.SetContentDecompressorKeys]({{% godoc v3 %}}Client.SetContentDecompressorKeys)
* [Client.ContentDecompressers]({{% godoc v3 %}}Client.ContentDecompressers)
* [Client.ContentDecompressorKeys]({{% godoc v3 %}}Client.ContentDecompressorKeys)
