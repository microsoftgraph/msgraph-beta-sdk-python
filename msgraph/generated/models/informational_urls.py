from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class InformationalUrls(AdditionalDataHolder, Parsable):
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
    def app_sign_up_url(self,) -> Optional[str]:
        """
        Gets the appSignUpUrl property value. The appSignUpUrl property
        Returns: Optional[str]
        """
        return self._app_sign_up_url
    
    @app_sign_up_url.setter
    def app_sign_up_url(self,value: Optional[str] = None) -> None:
        """
        Sets the appSignUpUrl property value. The appSignUpUrl property
        Args:
            value: Value to set for the appSignUpUrl property.
        """
        self._app_sign_up_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new informationalUrls and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The appSignUpUrl property
        self._app_sign_up_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The singleSignOnDocumentationUrl property
        self._single_sign_on_documentation_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationalUrls:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InformationalUrls
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InformationalUrls()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_sign_up_url": lambda n : setattr(self, 'app_sign_up_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "single_sign_on_documentation_url": lambda n : setattr(self, 'single_sign_on_documentation_url', n.get_str_value()),
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
        writer.write_str_value("appSignUpUrl", self.app_sign_up_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("singleSignOnDocumentationUrl", self.single_sign_on_documentation_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def single_sign_on_documentation_url(self,) -> Optional[str]:
        """
        Gets the singleSignOnDocumentationUrl property value. The singleSignOnDocumentationUrl property
        Returns: Optional[str]
        """
        return self._single_sign_on_documentation_url
    
    @single_sign_on_documentation_url.setter
    def single_sign_on_documentation_url(self,value: Optional[str] = None) -> None:
        """
        Sets the singleSignOnDocumentationUrl property value. The singleSignOnDocumentationUrl property
        Args:
            value: Value to set for the singleSignOnDocumentationUrl property.
        """
        self._single_sign_on_documentation_url = value
    

