from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

imported_apple_device_identity = lazy_import('msgraph.generated.models.imported_apple_device_identity')

class ImportAppleDeviceIdentityListPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the importAppleDeviceIdentityList method.
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new importAppleDeviceIdentityListPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The importedAppleDeviceIdentities property
        self._imported_apple_device_identities: Optional[List[imported_apple_device_identity.ImportedAppleDeviceIdentity]] = None
        # The overwriteImportedDeviceIdentities property
        self._overwrite_imported_device_identities: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImportAppleDeviceIdentityListPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImportAppleDeviceIdentityListPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ImportAppleDeviceIdentityListPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "imported_apple_device_identities": lambda n : setattr(self, 'imported_apple_device_identities', n.get_collection_of_object_values(imported_apple_device_identity.ImportedAppleDeviceIdentity)),
            "overwrite_imported_device_identities": lambda n : setattr(self, 'overwrite_imported_device_identities', n.get_bool_value()),
        }
        return fields
    
    @property
    def imported_apple_device_identities(self,) -> Optional[List[imported_apple_device_identity.ImportedAppleDeviceIdentity]]:
        """
        Gets the importedAppleDeviceIdentities property value. The importedAppleDeviceIdentities property
        Returns: Optional[List[imported_apple_device_identity.ImportedAppleDeviceIdentity]]
        """
        return self._imported_apple_device_identities
    
    @imported_apple_device_identities.setter
    def imported_apple_device_identities(self,value: Optional[List[imported_apple_device_identity.ImportedAppleDeviceIdentity]] = None) -> None:
        """
        Sets the importedAppleDeviceIdentities property value. The importedAppleDeviceIdentities property
        Args:
            value: Value to set for the importedAppleDeviceIdentities property.
        """
        self._imported_apple_device_identities = value
    
    @property
    def overwrite_imported_device_identities(self,) -> Optional[bool]:
        """
        Gets the overwriteImportedDeviceIdentities property value. The overwriteImportedDeviceIdentities property
        Returns: Optional[bool]
        """
        return self._overwrite_imported_device_identities
    
    @overwrite_imported_device_identities.setter
    def overwrite_imported_device_identities(self,value: Optional[bool] = None) -> None:
        """
        Sets the overwriteImportedDeviceIdentities property value. The overwriteImportedDeviceIdentities property
        Args:
            value: Value to set for the overwriteImportedDeviceIdentities property.
        """
        self._overwrite_imported_device_identities = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("importedAppleDeviceIdentities", self.imported_apple_device_identities)
        writer.write_bool_value("overwriteImportedDeviceIdentities", self.overwrite_imported_device_identities)
        writer.write_additional_data_value(self.additional_data)
    

