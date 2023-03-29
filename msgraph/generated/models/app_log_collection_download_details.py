from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_log_decryption_algorithm

class AppLogCollectionDownloadDetails(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new appLogCollectionDownloadDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The appLogDecryptionAlgorithm property
        self._app_log_decryption_algorithm: Optional[app_log_decryption_algorithm.AppLogDecryptionAlgorithm] = None
        # Decryption key that used to decrypt the log.
        self._decryption_key: Optional[str] = None
        # Download SAS (Shared Access Signature) Url for completed app log request.
        self._download_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def app_log_decryption_algorithm(self,) -> Optional[app_log_decryption_algorithm.AppLogDecryptionAlgorithm]:
        """
        Gets the appLogDecryptionAlgorithm property value. The appLogDecryptionAlgorithm property
        Returns: Optional[app_log_decryption_algorithm.AppLogDecryptionAlgorithm]
        """
        return self._app_log_decryption_algorithm
    
    @app_log_decryption_algorithm.setter
    def app_log_decryption_algorithm(self,value: Optional[app_log_decryption_algorithm.AppLogDecryptionAlgorithm] = None) -> None:
        """
        Sets the appLogDecryptionAlgorithm property value. The appLogDecryptionAlgorithm property
        Args:
            value: Value to set for the app_log_decryption_algorithm property.
        """
        self._app_log_decryption_algorithm = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppLogCollectionDownloadDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppLogCollectionDownloadDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppLogCollectionDownloadDetails()
    
    @property
    def decryption_key(self,) -> Optional[str]:
        """
        Gets the decryptionKey property value. Decryption key that used to decrypt the log.
        Returns: Optional[str]
        """
        return self._decryption_key
    
    @decryption_key.setter
    def decryption_key(self,value: Optional[str] = None) -> None:
        """
        Sets the decryptionKey property value. Decryption key that used to decrypt the log.
        Args:
            value: Value to set for the decryption_key property.
        """
        self._decryption_key = value
    
    @property
    def download_url(self,) -> Optional[str]:
        """
        Gets the downloadUrl property value. Download SAS (Shared Access Signature) Url for completed app log request.
        Returns: Optional[str]
        """
        return self._download_url
    
    @download_url.setter
    def download_url(self,value: Optional[str] = None) -> None:
        """
        Sets the downloadUrl property value. Download SAS (Shared Access Signature) Url for completed app log request.
        Args:
            value: Value to set for the download_url property.
        """
        self._download_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_log_decryption_algorithm

        fields: Dict[str, Callable[[Any], None]] = {
            "appLogDecryptionAlgorithm": lambda n : setattr(self, 'app_log_decryption_algorithm', n.get_enum_value(app_log_decryption_algorithm.AppLogDecryptionAlgorithm)),
            "decryptionKey": lambda n : setattr(self, 'decryption_key', n.get_str_value()),
            "downloadUrl": lambda n : setattr(self, 'download_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("appLogDecryptionAlgorithm", self.app_log_decryption_algorithm)
        writer.write_str_value("decryptionKey", self.decryption_key)
        writer.write_str_value("downloadUrl", self.download_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

