from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class MacOSAssociatedDomainsItem(AdditionalDataHolder, Parsable):
    """
    A mapping of application identifiers to associated domains.
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
    
    @property
    def application_identifier(self,) -> Optional[str]:
        """
        Gets the applicationIdentifier property value. The application identifier of the app to associate domains with.
        Returns: Optional[str]
        """
        return self._application_identifier
    
    @application_identifier.setter
    def application_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationIdentifier property value. The application identifier of the app to associate domains with.
        Args:
            value: Value to set for the applicationIdentifier property.
        """
        self._application_identifier = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new macOSAssociatedDomainsItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The application identifier of the app to associate domains with.
        self._application_identifier: Optional[str] = None
        # Determines whether data should be downloaded directly or via a CDN.
        self._direct_downloads_enabled: Optional[bool] = None
        # The list of domains to associate.
        self._domains: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSAssociatedDomainsItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSAssociatedDomainsItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSAssociatedDomainsItem()
    
    @property
    def direct_downloads_enabled(self,) -> Optional[bool]:
        """
        Gets the directDownloadsEnabled property value. Determines whether data should be downloaded directly or via a CDN.
        Returns: Optional[bool]
        """
        return self._direct_downloads_enabled
    
    @direct_downloads_enabled.setter
    def direct_downloads_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the directDownloadsEnabled property value. Determines whether data should be downloaded directly or via a CDN.
        Args:
            value: Value to set for the directDownloadsEnabled property.
        """
        self._direct_downloads_enabled = value
    
    @property
    def domains(self,) -> Optional[List[str]]:
        """
        Gets the domains property value. The list of domains to associate.
        Returns: Optional[List[str]]
        """
        return self._domains
    
    @domains.setter
    def domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the domains property value. The list of domains to associate.
        Args:
            value: Value to set for the domains property.
        """
        self._domains = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_identifier": lambda n : setattr(self, 'application_identifier', n.get_str_value()),
            "direct_downloads_enabled": lambda n : setattr(self, 'direct_downloads_enabled', n.get_bool_value()),
            "domains": lambda n : setattr(self, 'domains', n.get_collection_of_primitive_values(str)),
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
            value: Value to set for the OdataType property.
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
        writer.write_str_value("applicationIdentifier", self.application_identifier)
        writer.write_bool_value("directDownloadsEnabled", self.direct_downloads_enabled)
        writer.write_collection_of_primitive_values("domains", self.domains)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

