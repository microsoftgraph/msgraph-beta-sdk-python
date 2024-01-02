from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ApplicationDetail(AdditionalDataHolder, BackedModel, Parsable):
    """
    The details of the application which the user has requested to elevate
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The path of the file in the request for elevation, for example, %programfiles%/git/cmd
    file_description: Optional[str] = None
    # The SHA256 hash of the file in the request for elevation, for example, '18ee24150dcb1d96752a4d6dd0f20dfd8ba8c38527e40aa8509b7adecf78f9c6'
    file_hash: Optional[str] = None
    # The name of the file in the request for elevation, for example, git.exe
    file_name: Optional[str] = None
    # The path of the file in the request for elevation, for example, %programfiles%/git/cmd
    file_path: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The internal name of the application for which elevation request has been made. For example, 'git'
    product_internal_name: Optional[str] = None
    # The product name of the application for which elevation request has been made. For example, 'Git'
    product_name: Optional[str] = None
    # The product version of the application for which elevation request has been made. For example, '2.40.1.0'
    product_version: Optional[str] = None
    # The certificate issuer name of the certificate used to sign the application, for example, 'Sectigo Public Code Signing CA R36'
    publisher_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplicationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ApplicationDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "fileDescription": lambda n : setattr(self, 'file_description', n.get_str_value()),
            "fileHash": lambda n : setattr(self, 'file_hash', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "filePath": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "productInternalName": lambda n : setattr(self, 'product_internal_name', n.get_str_value()),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "productVersion": lambda n : setattr(self, 'product_version', n.get_str_value()),
            "publisherName": lambda n : setattr(self, 'publisher_name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("fileDescription", self.file_description)
        writer.write_str_value("fileHash", self.file_hash)
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("filePath", self.file_path)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("productInternalName", self.product_internal_name)
        writer.write_str_value("productName", self.product_name)
        writer.write_str_value("productVersion", self.product_version)
        writer.write_str_value("publisherName", self.publisher_name)
        writer.write_additional_data_value(self.additional_data)
    

