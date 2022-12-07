from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class CloudPcForensicStorageAccount(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcForensicStorageAccount and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The ID of the storage account.
        self._storage_account_id: Optional[str] = None
        # The name of the storage account.
        self._storage_account_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcForensicStorageAccount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcForensicStorageAccount
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcForensicStorageAccount()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "storage_account_id": lambda n : setattr(self, 'storage_account_id', n.get_str_value()),
            "storage_account_name": lambda n : setattr(self, 'storage_account_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("storageAccountId", self.storage_account_id)
        writer.write_str_value("storageAccountName", self.storage_account_name)
    
    @property
    def storage_account_id(self,) -> Optional[str]:
        """
        Gets the storageAccountId property value. The ID of the storage account.
        Returns: Optional[str]
        """
        return self._storage_account_id
    
    @storage_account_id.setter
    def storage_account_id(self,value: Optional[str] = None) -> None:
        """
        Sets the storageAccountId property value. The ID of the storage account.
        Args:
            value: Value to set for the storageAccountId property.
        """
        self._storage_account_id = value
    
    @property
    def storage_account_name(self,) -> Optional[str]:
        """
        Gets the storageAccountName property value. The name of the storage account.
        Returns: Optional[str]
        """
        return self._storage_account_name
    
    @storage_account_name.setter
    def storage_account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the storageAccountName property value. The name of the storage account.
        Args:
            value: Value to set for the storageAccountName property.
        """
        self._storage_account_name = value
    

